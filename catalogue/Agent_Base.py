"""
BASE CLASS: Agent_Base
======================

Core agent template for all MAaaS agents. Provides common functionality
and MCP (Model Context Protocol) capability for external tool access.

This base class implements the "Code Mode" strategy where agents dynamically
discover and use external tools via the Universal MCP Client.
"""

import uuid
from datetime import datetime
from typing import Dict, Optional, List, Any


class Agent_Base:
    """
    BASE CLASS: Agent_Base
    ======================
    
    Core agent template providing:
    - Common agent lifecycle (contract signing, delegation)
    - MCP capability for external tool discovery and execution
    - Standard agent interface
    
    CAPABILITY: External Tool Access via MCP
    =========================================
    
    Agents can dynamically discover and use external tools through the
    Universal MCP Client. This enables "Code Mode" where agents generate
    Python scripts to interact with external systems rather than having
    hardcoded tool definitions.
    
    MCP API Reference:
    ------------------
    
    Import the Universal MCP Client:
        from tools.Universal_MCP_Client import create_stdio_client, create_sse_client
    
    Basic Usage Pattern:
        1. Connect to MCP server:
           client = create_stdio_client(["node", "mcp-server.js"])
           client.connect()
        
        2. Discover available tools (lightweight):
           tools = client.list_tools()
           # Returns: ["tool1", "tool2", "tool3", ...]
        
        3. Get tool schema when needed:
           schema = client.get_tool_schema("tool_name")
           # Returns: {
           #   "name": "tool_name",
           #   "description": "Tool description",
           #   "inputSchema": {...}  # JSON schema for parameters
           # }
        
        4. Execute tool:
           result = client.call_tool("tool_name", {"arg1": "value1", "arg2": "value2"})
           # Returns: {"content": [...], "isError": false}
        
        5. Cleanup:
           client.disconnect()
    
    Context Manager Pattern (Recommended):
        with create_stdio_client(["node", "mcp-server.js"]) as client:
            tools = client.list_tools()
            if "desired_tool" in tools:
                schema = client.get_tool_schema("desired_tool")
                result = client.call_tool("desired_tool", {...})
    
    Error Handling:
        from tools.Universal_MCP_Client import (
            MCPConnectionError,
            MCPExecutionError,
            MCPTimeoutError
        )
        
        try:
            result = client.call_tool("tool_name", {...})
        except MCPConnectionError as e:
            # Connection failed - agent should retry or report
        except MCPExecutionError as e:
            # Tool execution failed - agent can self-correct
        except MCPTimeoutError as e:
            # Operation timed out - agent should retry
    
    Transport Types:
    ---------------
    
    stdio (Standard Input/Output):
        For subprocess-based MCP servers (e.g., Node.js, Python scripts)
        client = create_stdio_client(["node", "mcp-server.js"])
        client = create_stdio_client(["python", "mcp_server.py"])
    
    SSE (Server-Sent Events):
        For HTTP-based MCP servers
        client = create_sse_client("http://localhost:3000/mcp")
    
    Guidance for Agents:
    -------------------
    
    When to Use MCP:
    - When you need to interact with external systems (GitHub, file systems, databases)
    - When you need to discover available tools dynamically
    - When tool definitions are not known at agent initialization time
    
    How to Use MCP:
    1. Identify the need for an external tool (e.g., "I need to read a file",
       "I need to query GitHub", "I need to access a database")
    
    2. Write a Python script that:
       a. Connects to the MCP server
       b. Lists available tools to discover what's available
       c. Gets the schema for the relevant tool
       d. Executes the tool with proper arguments
       e. Handles errors gracefully
    
    3. Do NOT hallucinate tools that are not listed by list_tools()
       - Always call list_tools() first to see what's available
       - If a tool doesn't exist, report this clearly rather than assuming it exists
    
    4. Example Agent-Generated Code:
       ```python
       from tools.Universal_MCP_Client import create_stdio_client
       
       def discover_and_use_file_tool():
           \"\"\"Agent discovers file system tools via MCP.\"\"\"
           with create_stdio_client(["node", "mcp-filesystem.js"]) as client:
               # Discover available tools
               available_tools = client.list_tools()
               
               # Find file-related tool
               file_tool = None
               for tool in available_tools:
                   if "file" in tool.lower() or "read" in tool.lower():
                       file_tool = tool
                       break
               
               if not file_tool:
                   return {"error": "No file tool available"}
               
               # Get schema to understand parameters
               schema = client.get_tool_schema(file_tool)
               
               # Execute with proper arguments
               result = client.call_tool(
                   file_tool,
                   {"path": "/path/to/file.txt", "operation": "read"}
               )
               
               return result
       ```
    
    Security Considerations:
    -----------------------
    - Always validate tool inputs against the schema before calling
    - Respect MPC (Multi-Party Computation) requirements when handling sensitive data
    - Log all MCP tool calls for provenance tracking (C5 compliance)
    - Use session firewalls when required by contract (C6 compliance)
    """
    
    def __init__(self, agent_name: str, role: str = "BaseAgent"):
        """
        Initialize the base agent.
        
        Args:
            agent_name: Human-readable name for this agent instance
            role: Agent role (e.g., "Researcher", "Compliance", "ProjectManager")
        """
        self.agent_id = str(uuid.uuid4())
        self.name = agent_name
        self.role = role
        self.active_contract: Optional[Dict] = None
        self.created_at = datetime.now().isoformat()
    
    def sign_contract(self, contract_json: Dict) -> bool:
        """
        Sign an E-Contract for this agent.
        
        Base implementation validates required keys. Subclasses should
        override to add role-specific validation.
        
        Args:
            contract_json: Contract dictionary with required keys
            
        Returns:
            True if contract is valid and signed, False otherwise
        """
        required_keys = ["contract_id", "security_protocols"]
        if not all(k in contract_json for k in required_keys):
            print(f"[{self.role}-ERROR] Contract {contract_json.get('contract_id')} rejected: Malformed.")
            return False
        
        # Check for Security Compliance
        security = contract_json.get("security_protocols", {})
        if not security.get("mpc_required", False):
            print(f"[{self.role}-WARNING] Agent {self.name} notes lack of MPC requirement. Privacy risk elevated.")
        
        if not security.get("session_firewall_enabled", False):
            print(f"[{self.role}-WARNING] Missing Session Firewall (risk of context bypass C6).")
        
        self.active_contract = contract_json
        self.active_contract["status"] = "SIGNED"
        self.active_contract["signed_at"] = datetime.now().isoformat()
        
        print(f"[{self.role}-INFO] Agent {self.name} accepted Contract {contract_json['contract_id']}.")
        return True
    
    def delegate(self, task: Dict, target_agent_id: str) -> Dict:
        """
        Delegate a task to another agent.
        
        Args:
            task: Task dictionary with task details
            target_agent_id: ID of the target agent
            
        Returns:
            Message dictionary for A2A protocol
            
        Raises:
            PermissionError: If agent doesn't have a signed contract
        """
        if not self.active_contract or self.active_contract.get("status") != "SIGNED":
            raise PermissionError(f"Cannot delegate without a signed contract.")
        
        message = {
            "from": self.agent_id,
            "to": target_agent_id,
            "type": "TASK_ASSIGNMENT",
            "payload": task,
            "context_file": "Client_SOPs.md",
            "timestamp": datetime.now().isoformat()
        }
        
        print(f"[{self.role}-DELEGATION] {self.name} delegated task '{task.get('task', 'unknown')}' to Agent {target_agent_id}.")
        return message
    
    def to_json(self) -> Dict:
        """
        Serialize agent to JSON representation.
        
        Returns:
            Dictionary with agent metadata
        """
        return {
            "agent_id": self.agent_id,
            "role": self.role,
            "name": self.name,
            "status": "ACTIVE" if self.active_contract else "IDLE",
            "contract_id": self.active_contract.get("contract_id") if self.active_contract else None,
            "created_at": self.created_at
        }
    
    def get_mcp_usage_instructions(self) -> str:
        """
        Get MCP usage instructions as a formatted string.
        
        This can be included in agent system prompts or documentation.
        
        Returns:
            Formatted string with MCP usage instructions
        """
        return """
CAPABILITY: External Tool Access via MCP
========================================

You have access to the Universal MCP Client for discovering and using external tools.

Quick Start:
    from tools.Universal_MCP_Client import create_stdio_client
    
    with create_stdio_client(["node", "mcp-server.js"]) as client:
        tools = client.list_tools()           # Discover available tools
        schema = client.get_tool_schema(name)  # Get tool definition
        result = client.call_tool(name, args)  # Execute tool

Important Rules:
1. Always call list_tools() first to see what's available
2. Do NOT hallucinate tools - only use tools returned by list_tools()
3. Get the schema before executing to understand required parameters
4. Handle errors gracefully and self-correct based on error messages
5. Use context manager (with statement) for automatic cleanup
        """
    
    def __repr__(self) -> str:
        """String representation of the agent."""
        return f"<{self.__class__.__name__}(name='{self.name}', role='{self.role}', status={'ACTIVE' if self.active_contract else 'IDLE'})>"


# System prompt template for LLM agents
AGENT_SYSTEM_PROMPT_TEMPLATE = """
You are {agent_name}, a {role} agent in the MAaaS (Multi-Agent as a Service) platform.

{role_specific_instructions}

CAPABILITY: External Tool Access via MCP
========================================

You can discover and use external tools dynamically through the Universal MCP Client.

MCP API Reference:
-----------------

Import:
    from tools.Universal_MCP_Client import create_stdio_client, create_sse_client

Basic Operations:
    1. Connect: client = create_stdio_client(["node", "mcp-server.js"])
    2. Discover: tools = client.list_tools()  # Returns list of tool names
    3. Get Schema: schema = client.get_tool_schema("tool_name")
    4. Execute: result = client.call_tool("tool_name", {{"arg": "value"}})
    5. Cleanup: client.disconnect() or use context manager

Recommended Pattern:
    with create_stdio_client(["node", "mcp-server.js"]) as client:
        available_tools = client.list_tools()
        if "desired_tool" in available_tools:
            schema = client.get_tool_schema("desired_tool")
            result = client.call_tool("desired_tool", {{...}})

Critical Rules:
---------------
1. ALWAYS call list_tools() first to discover available tools
2. NEVER hallucinate tools - only use tools that exist in the list
3. Get the schema before executing to understand parameters
4. Handle errors gracefully (MCPConnectionError, MCPExecutionError, MCPTimeoutError)
5. If a tool doesn't exist, report this clearly - do not assume it exists

When to Use MCP:
- When you need external system access (GitHub, file systems, databases)
- When tool definitions are not known at initialization
- When you need to discover capabilities dynamically

Example Agent-Generated Code:
    from tools.Universal_MCP_Client import create_stdio_client
    
    def use_external_tool():
        with create_stdio_client(["node", "mcp-server.js"]) as client:
            tools = client.list_tools()
            if "file_reader" in tools:
                result = client.call_tool("file_reader", {{"path": "/file.txt"}})
                return result
            else:
                return {{"error": "file_reader tool not available"}}

Security:
---------
- Validate inputs against tool schema
- Respect MPC requirements for sensitive data
- Log all MCP calls for provenance (C5 compliance)
- Use session firewalls when required (C6 compliance)
"""


def generate_agent_system_prompt(agent_name: str, role: str, role_specific_instructions: str = "") -> str:
    """
    Generate a system prompt for an LLM agent with MCP capability.
    
    Args:
        agent_name: Name of the agent
        role: Role of the agent
        role_specific_instructions: Additional role-specific instructions
        
    Returns:
        Formatted system prompt string
    """
    return AGENT_SYSTEM_PROMPT_TEMPLATE.format(
        agent_name=agent_name,
        role=role,
        role_specific_instructions=role_specific_instructions
    )

