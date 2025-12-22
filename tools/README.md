# Universal MCP Client Bridge

A protocol-agnostic client for connecting to Model Context Protocol (MCP) servers. This enables the "Code Mode" strategy where agents dynamically discover and use external tools.

## Features

- **Protocol Agnostic**: Supports both stdio and SSE transports
- **Lightweight Discovery**: `list_tools()` returns only tool names
- **On-Demand Schemas**: `get_tool_schema()` retrieves full API definitions when needed
- **Secure Execution**: `call_tool()` executes tools with proper error handling
- **Clean Error Messages**: All errors return human-readable descriptions for agent self-correction

## Quick Start

### stdio Transport

```python
from tools.Universal_MCP_Client import create_stdio_client

# Connect to MCP server via subprocess
client = create_stdio_client(["node", "mcp-server.js"])
client.connect()

# Discover available tools
tools = client.list_tools()
print(f"Available tools: {tools}")

# Get schema for a specific tool
schema = client.get_tool_schema("tool_name")
print(f"Schema: {schema}")

# Execute a tool
result = client.call_tool("tool_name", {"arg1": "value1", "arg2": "value2"})
print(f"Result: {result}")

client.disconnect()
```

### SSE Transport

```python
from tools.Universal_MCP_Client import create_sse_client

# Connect to MCP server via HTTP/SSE
client = create_sse_client("http://localhost:3000/mcp")
client.connect()

# Use the same API
tools = client.list_tools()
result = client.call_tool("tool_name", {"arg1": "value1"})

client.disconnect()
```

### Context Manager

```python
from tools.Universal_MCP_Client import create_stdio_client

# Automatic connection/disconnection
with create_stdio_client(["node", "mcp-server.js"]) as client:
    tools = client.list_tools()
    if tools:
        schema = client.get_tool_schema(tools[0])
        result = client.call_tool(tools[0], {"param": "value"})
```

## Agent Code Mode Usage

Agents can generate code to discover and use tools dynamically:

```python
# Agent-generated code example
from tools.Universal_MCP_Client import create_stdio_client

def discover_and_use_tools():
    """Agent discovers available tools and uses them."""
    client = create_stdio_client(["node", "mcp-server.js"])
    client.connect()
    
    try:
        # Step 1: Discover tools (lightweight)
        available_tools = client.list_tools()
        
        # Step 2: Find relevant tool
        relevant_tool = None
        for tool_name in available_tools:
            if "pdf" in tool_name.lower() or "parser" in tool_name.lower():
                relevant_tool = tool_name
                break
        
        if not relevant_tool:
            return {"error": "No suitable tool found"}
        
        # Step 3: Get schema (only when needed)
        schema = client.get_tool_schema(relevant_tool)
        
        # Step 4: Execute with proper arguments
        result = client.call_tool(
            relevant_tool,
            {
                "file_path": "/path/to/file.pdf",
                "options": {"extract_text": True}
            }
        )
        
        return {"success": True, "result": result}
        
    except Exception as e:
        return {"error": str(e)}
    finally:
        client.disconnect()
```

## Error Handling

All errors return clean, descriptive messages:

```python
from tools.Universal_MCP_Client import (
    UniversalMCPClient,
    MCPConnectionError,
    MCPExecutionError,
    MCPTimeoutError
)

try:
    client = create_stdio_client(["node", "mcp-server.js"])
    client.connect()
    result = client.call_tool("nonexistent_tool", {})
except MCPConnectionError as e:
    print(f"Connection failed: {e}")
except MCPExecutionError as e:
    print(f"Tool execution failed: {e}")
except MCPTimeoutError as e:
    print(f"Operation timed out: {e}")
```

## API Reference

### `list_tools() -> List[str]`

Returns a lightweight list of available tool names only. Cached for performance.

**Returns:** List of tool name strings

**Raises:**
- `MCPConnectionError`: If not connected
- `MCPExecutionError`: If server returns an error

### `get_tool_schema(tool_name: str) -> Dict[str, Any]`

Retrieves the full schema/definition for a specific tool. Includes:
- `name`: Tool name
- `description`: Tool description
- `inputSchema`: JSON schema for parameters

**Returns:** Dictionary with tool schema

**Raises:**
- `MCPConnectionError`: If not connected
- `MCPExecutionError`: If tool not found

### `call_tool(tool_name: str, arguments: Dict[str, Any]) -> Dict[str, Any]`

Executes a tool with the given arguments.

**Returns:** Dictionary with tool execution result

**Raises:**
- `MCPConnectionError`: If not connected
- `MCPExecutionError`: If execution fails
- `MCPTimeoutError`: If execution times out

## Transport Types

### stdio (Standard Input/Output)

Used for subprocess-based MCP servers:

```python
client = UniversalMCPClient(
    transport=TransportType.STDIO,
    command=["node", "mcp-server.js"],
    timeout=30
)
```

### SSE (Server-Sent Events)

Used for HTTP-based MCP servers:

```python
client = UniversalMCPClient(
    transport=TransportType.SSE,
    url="http://localhost:3000/mcp",
    timeout=30,
    request_timeout=60
)
```

## Caching

The client caches tool lists and schemas for performance:

```python
# First call fetches from server
tools = client.list_tools()

# Subsequent calls use cache
tools2 = client.list_tools()  # Fast, uses cache

# Clear cache if needed
client.clear_cache()
```

## Requirements

- Python 3.9+
- `requests` library (for SSE transport)

Already included in `requirements.txt`.

