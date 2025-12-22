#!/usr/bin/env python3
"""
Universal MCP Client Bridge
============================

A protocol-agnostic client for connecting to Model Context Protocol (MCP) servers.
Supports both stdio (Standard Input/Output) and SSE (Server-Sent Events) transports.

This client enables "Code Mode" strategy where agents can dynamically discover
and use external tools without hardcoded definitions in system prompts.

Reference: Model Context Protocol (MCP) Specification
"""

import json
import subprocess
import sys
import threading
import time
from enum import Enum
from typing import Dict, List, Optional, Any, Union
from pathlib import Path
import requests
from datetime import datetime


class TransportType(Enum):
    """Supported transport types for MCP connections."""
    STDIO = "stdio"
    SSE = "sse"


class MCPError(Exception):
    """Base exception for MCP client errors."""
    pass


class MCPConnectionError(MCPError):
    """Raised when connection to MCP server fails."""
    pass


class MCPExecutionError(MCPError):
    """Raised when tool execution fails."""
    pass


class MCPTimeoutError(MCPError):
    """Raised when operation times out."""
    pass


class UniversalMCPClient:
    """
    Universal MCP Client for protocol-agnostic tool discovery and execution.
    
    This client supports:
    - stdio transport: Subprocess-based communication
    - SSE transport: HTTP-based Server-Sent Events
    
    Usage:
        # stdio transport
        client = UniversalMCPClient(
            transport=TransportType.STDIO,
            command=["node", "mcp-server.js"]
        )
        
        # SSE transport
        client = UniversalMCPClient(
            transport=TransportType.SSE,
            url="http://localhost:3000/mcp"
        )
        
        # Discover tools
        tools = client.list_tools()
        
        # Get schema
        schema = client.get_tool_schema("tool_name")
        
        # Execute tool
        result = client.call_tool("tool_name", {"arg1": "value1"})
    """
    
    def __init__(
        self,
        transport: TransportType,
        command: Optional[List[str]] = None,
        url: Optional[str] = None,
        timeout: int = 30,
        request_timeout: int = 60
    ):
        """
        Initialize the Universal MCP Client.
        
        Args:
            transport: Transport type (STDIO or SSE)
            command: For stdio transport, the command to start the MCP server
            url: For SSE transport, the base URL of the MCP server
            timeout: Timeout for operations in seconds
            request_timeout: Timeout for HTTP requests (SSE only)
        """
        self.transport = transport
        self.timeout = timeout
        self.request_timeout = request_timeout
        self._request_id_counter = 0
        self._request_lock = threading.Lock()
        self._pending_requests: Dict[int, Dict[str, Any]] = {}
        self._tool_cache: Optional[List[str]] = None
        self._schema_cache: Dict[str, Dict[str, Any]] = {}
        
        # Transport-specific initialization
        if transport == TransportType.STDIO:
            if not command:
                raise ValueError("command is required for stdio transport")
            self.command = command
            self.process: Optional[subprocess.Popen] = None
            self._stdio_thread: Optional[threading.Thread] = None
            self._stdio_buffer: List[str] = []
            self._stdio_lock = threading.Lock()
        elif transport == TransportType.SSE:
            if not url:
                raise ValueError("url is required for SSE transport")
            self.url = url.rstrip('/')
            self.session = requests.Session()
            self.session.timeout = request_timeout
        else:
            raise ValueError(f"Unsupported transport type: {transport}")
    
    def _generate_request_id(self) -> int:
        """Generate a unique request ID for JSON-RPC."""
        with self._request_lock:
            self._request_id_counter += 1
            return self._request_id_counter
    
    def _create_jsonrpc_request(self, method: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Create a JSON-RPC 2.0 request."""
        return {
            "jsonrpc": "2.0",
            "id": self._generate_request_id(),
            "method": method,
            "params": params or {}
        }
    
    def connect(self) -> bool:
        """
        Establish connection to the MCP server.
        
        Returns:
            True if connection successful, False otherwise
            
        Raises:
            MCPConnectionError: If connection fails
        """
        try:
            if self.transport == TransportType.STDIO:
                return self._connect_stdio()
            elif self.transport == TransportType.SSE:
                return self._connect_sse()
        except Exception as e:
            raise MCPConnectionError(f"Failed to connect to MCP server: {str(e)}")
    
    def _connect_stdio(self) -> bool:
        """Connect via stdio transport."""
        try:
            self.process = subprocess.Popen(
                self.command,
                stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                text=True,
                bufsize=0
            )
            
            # Start thread to read stdout
            self._stdio_thread = threading.Thread(
                target=self._read_stdio_output,
                daemon=True
            )
            self._stdio_thread.start()
            
            # Wait a moment for server to initialize
            time.sleep(0.5)
            
            # Test connection with initialize request
            return self._test_connection()
        except Exception as e:
            raise MCPConnectionError(f"stdio connection failed: {str(e)}")
    
    def _connect_sse(self) -> bool:
        """Connect via SSE transport."""
        try:
            # Test connection with health check or initialize
            response = self.session.get(f"{self.url}/health", timeout=5)
            if response.status_code == 200:
                return True
            # If no health endpoint, try to initialize
            return self._test_connection()
        except requests.exceptions.RequestException as e:
            raise MCPConnectionError(f"SSE connection failed: {str(e)}")
    
    def _test_connection(self) -> bool:
        """Test the connection by attempting to list tools."""
        try:
            # Try a lightweight operation
            self.list_tools()
            return True
        except Exception:
            return False
    
    def _read_stdio_output(self):
        """Background thread to read stdout from stdio process."""
        if not self.process or not self.process.stdout:
            return
        
        buffer = ""
        while True:
            try:
                # Read line by line (MCP servers typically send one JSON-RPC message per line)
                line = self.process.stdout.readline()
                if not line:
                    break
                
                line = line.strip()
                if not line:
                    continue
                
                try:
                    response = json.loads(line)
                    self._handle_stdio_response(response)
                except json.JSONDecodeError:
                    # If not valid JSON, try to accumulate (for multi-line JSON)
                    buffer += line
                    try:
                        response = json.loads(buffer)
                        self._handle_stdio_response(response)
                        buffer = ""
                    except json.JSONDecodeError:
                        # Still incomplete, keep accumulating
                        if len(buffer) > 10000:  # Prevent buffer overflow
                            buffer = ""
                        continue
            except Exception:
                break
    
    def _handle_stdio_response(self, response: Dict[str, Any]):
        """Handle response from stdio transport."""
        request_id = response.get("id")
        if request_id in self._pending_requests:
            with self._stdio_lock:
                self._pending_requests[request_id] = response
    
    def disconnect(self):
        """Disconnect from the MCP server."""
        if self.transport == TransportType.STDIO:
            if self.process:
                try:
                    self.process.terminate()
                    self.process.wait(timeout=5)
                except subprocess.TimeoutExpired:
                    self.process.kill()
                except Exception:
                    pass
                finally:
                    self.process = None
        elif self.transport == TransportType.SSE:
            self.session.close()
    
    def _send_request_stdio(self, request: Dict[str, Any]) -> Dict[str, Any]:
        """Send request via stdio transport and wait for response."""
        if not self.process or not self.process.stdin:
            raise MCPConnectionError("Not connected to MCP server")
        
        request_id = request["id"]
        request_str = json.dumps(request) + "\n"
        
        # Register pending request
        with self._request_lock:
            self._pending_requests[request_id] = {"status": "pending"}
        
        try:
            # Send request
            self.process.stdin.write(request_str)
            self.process.stdin.flush()
            
            # Wait for response
            start_time = time.time()
            while time.time() - start_time < self.timeout:
                with self._stdio_lock:
                    if request_id in self._pending_requests:
                        response = self._pending_requests[request_id]
                        if response.get("status") != "pending":
                            del self._pending_requests[request_id]
                            if "error" in response:
                                raise MCPExecutionError(
                                    f"MCP server error: {response['error'].get('message', 'Unknown error')}"
                                )
                            return response
                time.sleep(0.1)
            
            # Timeout
            with self._request_lock:
                if request_id in self._pending_requests:
                    del self._pending_requests[request_id]
            raise MCPTimeoutError(f"Request timed out after {self.timeout} seconds")
            
        except Exception as e:
            with self._request_lock:
                if request_id in self._pending_requests:
                    del self._pending_requests[request_id]
            raise MCPExecutionError(f"Failed to send request: {str(e)}")
    
    def _send_request_sse(self, request: Dict[str, Any]) -> Dict[str, Any]:
        """Send request via SSE transport."""
        try:
            response = self.session.post(
                f"{self.url}/jsonrpc",
                json=request,
                headers={"Content-Type": "application/json"},
                timeout=self.request_timeout
            )
            response.raise_for_status()
            result = response.json()
            
            if "error" in result:
                error_msg = result["error"].get("message", "Unknown error")
                raise MCPExecutionError(f"MCP server error: {error_msg}")
            
            return result
            
        except requests.exceptions.Timeout:
            raise MCPTimeoutError(f"Request timed out after {self.request_timeout} seconds")
        except requests.exceptions.RequestException as e:
            raise MCPConnectionError(f"SSE request failed: {str(e)}")
    
    def _send_request(self, method: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
        """Send a JSON-RPC request and return the response."""
        request = self._create_jsonrpc_request(method, params)
        
        if self.transport == TransportType.STDIO:
            return self._send_request_stdio(request)
        elif self.transport == TransportType.SSE:
            return self._send_request_sse(request)
    
    def list_tools(self) -> List[str]:
        """
        List available tools (lightweight - returns only tool names).
        
        Returns:
            List of tool names available on the MCP server
            
        Raises:
            MCPConnectionError: If not connected
            MCPExecutionError: If server returns an error
        """
        try:
            # Use cached result if available
            if self._tool_cache is not None:
                return self._tool_cache
            
            # Send tools/list request
            response = self._send_request("tools/list")
            
            # Extract tool names
            tools = response.get("result", {}).get("tools", [])
            tool_names = [tool.get("name", "") for tool in tools if tool.get("name")]
            
            # Cache the result
            self._tool_cache = tool_names
            
            return tool_names
            
        except MCPError:
            raise
        except Exception as e:
            raise MCPExecutionError(f"Failed to list tools: {str(e)}")
    
    def get_tool_schema(self, tool_name: str) -> Dict[str, Any]:
        """
        Get the full schema/definition for a specific tool.
        
        Args:
            tool_name: Name of the tool to get schema for
            
        Returns:
            Dictionary containing the tool schema including:
            - name: Tool name
            - description: Tool description
            - inputSchema: JSON schema for tool parameters
            
        Raises:
            MCPConnectionError: If not connected
            MCPExecutionError: If tool not found or server error
        """
        try:
            # Check cache first
            if tool_name in self._schema_cache:
                return self._schema_cache[tool_name]
            
            # Get all tools to find the one we need
            response = self._send_request("tools/list")
            tools = response.get("result", {}).get("tools", [])
            
            # Find the requested tool
            tool_schema = None
            for tool in tools:
                if tool.get("name") == tool_name:
                    tool_schema = tool
                    break
            
            if not tool_schema:
                raise MCPExecutionError(f"Tool '{tool_name}' not found on MCP server")
            
            # Cache the schema
            self._schema_cache[tool_name] = tool_schema
            
            return tool_schema
            
        except MCPError:
            raise
        except Exception as e:
            raise MCPExecutionError(f"Failed to get tool schema for '{tool_name}': {str(e)}")
    
    def call_tool(self, tool_name: str, arguments: Dict[str, Any]) -> Dict[str, Any]:
        """
        Execute a tool with the given arguments.
        
        Args:
            tool_name: Name of the tool to execute
            arguments: Dictionary of arguments to pass to the tool
            
        Returns:
            Dictionary containing the tool execution result
            
        Raises:
            MCPConnectionError: If not connected
            MCPExecutionError: If tool execution fails
            MCPTimeoutError: If execution times out
        """
        try:
            # Send tools/call request
            response = self._send_request(
                "tools/call",
                {
                    "name": tool_name,
                    "arguments": arguments
                }
            )
            
            result = response.get("result", {})
            
            # Check for errors in result
            if "error" in result:
                error_msg = result["error"].get("message", "Unknown error")
                raise MCPExecutionError(f"Tool '{tool_name}' execution failed: {error_msg}")
            
            return result
            
        except MCPError:
            raise
        except Exception as e:
            if isinstance(e, MCPError):
                raise
            raise MCPExecutionError(f"Failed to execute tool '{tool_name}': {str(e)}")
    
    def clear_cache(self):
        """Clear cached tool lists and schemas."""
        self._tool_cache = None
        self._schema_cache.clear()
    
    def __enter__(self):
        """Context manager entry."""
        self.connect()
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit."""
        self.disconnect()
    
    def __del__(self):
        """Cleanup on deletion."""
        try:
            self.disconnect()
        except Exception:
            pass


# Convenience functions for common use cases

def create_stdio_client(command: List[str], timeout: int = 30) -> UniversalMCPClient:
    """
    Create an MCP client using stdio transport.
    
    Args:
        command: Command to start the MCP server (e.g., ["node", "server.js"])
        timeout: Operation timeout in seconds
        
    Returns:
        Configured UniversalMCPClient instance
    """
    return UniversalMCPClient(
        transport=TransportType.STDIO,
        command=command,
        timeout=timeout
    )


def create_sse_client(url: str, timeout: int = 30, request_timeout: int = 60) -> UniversalMCPClient:
    """
    Create an MCP client using SSE transport.
    
    Args:
        url: Base URL of the MCP server (e.g., "http://localhost:3000/mcp")
        timeout: Operation timeout in seconds
        request_timeout: HTTP request timeout in seconds
        
    Returns:
        Configured UniversalMCPClient instance
    """
    return UniversalMCPClient(
        transport=TransportType.SSE,
        url=url,
        timeout=timeout,
        request_timeout=request_timeout
    )


# Example usage
if __name__ == "__main__":
    # Example 1: stdio transport
    print("Example 1: stdio transport")
    try:
        client = create_stdio_client(["node", "mcp-server.js"])
        client.connect()
        
        # List tools
        tools = client.list_tools()
        print(f"Available tools: {tools}")
        
        # Get schema for first tool
        if tools:
            schema = client.get_tool_schema(tools[0])
            print(f"Schema for '{tools[0]}': {json.dumps(schema, indent=2)}")
        
        client.disconnect()
    except Exception as e:
        print(f"Error: {e}")
    
    # Example 2: SSE transport
    print("\nExample 2: SSE transport")
    try:
        client = create_sse_client("http://localhost:3000/mcp")
        client.connect()
        
        # List tools
        tools = client.list_tools()
        print(f"Available tools: {tools}")
        
        # Execute a tool
        if tools:
            result = client.call_tool(tools[0], {"arg1": "value1"})
            print(f"Tool result: {json.dumps(result, indent=2)}")
        
        client.disconnect()
    except Exception as e:
        print(f"Error: {e}")
    
    # Example 3: Context manager
    print("\nExample 3: Using context manager")
    try:
        with create_stdio_client(["node", "mcp-server.js"]) as client:
            tools = client.list_tools()
            print(f"Available tools: {tools}")
    except Exception as e:
        print(f"Error: {e}")

