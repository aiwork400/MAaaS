# MCP Usage Example for Agents

This document shows how agents can use the Universal MCP Client based on the instructions in `Agent_Base`.

## Example: Agent Discovering and Using File System Tools

```python
from tools.Universal_MCP_Client import create_stdio_client, MCPExecutionError

def agent_use_file_tools():
    """
    Example of an agent discovering and using file system tools via MCP.
    This follows the "Code Mode" strategy where the agent generates code
    to discover tools dynamically.
    """
    try:
        # Step 1: Connect to MCP server
        with create_stdio_client(["node", "mcp-filesystem.js"]) as client:
            # Step 2: Discover available tools (lightweight)
            available_tools = client.list_tools()
            print(f"Available tools: {available_tools}")
            
            # Step 3: Find relevant tool
            file_tool = None
            for tool in available_tools:
                if "file" in tool.lower() or "read" in tool.lower():
                    file_tool = tool
                    break
            
            if not file_tool:
                return {"error": "No file tool available on MCP server"}
            
            # Step 4: Get schema to understand parameters
            schema = client.get_tool_schema(file_tool)
            print(f"Tool schema: {schema}")
            
            # Step 5: Execute tool with proper arguments
            result = client.call_tool(
                file_tool,
                {
                    "path": "/path/to/file.txt",
                    "operation": "read"
                }
            )
            
            return {"success": True, "result": result}
            
    except MCPExecutionError as e:
        # Agent can self-correct based on error message
        return {"error": f"Tool execution failed: {str(e)}"}
```

## Example: Agent Using GitHub Tools

```python
from tools.Universal_MCP_Client import create_sse_client

def agent_use_github_tools():
    """
    Example of an agent using GitHub tools via SSE transport.
    """
    try:
        with create_sse_client("http://localhost:3000/mcp-github") as client:
            # Discover tools
            tools = client.list_tools()
            
            # Find GitHub-related tools
            github_tools = [t for t in tools if "github" in t.lower()]
            
            if not github_tools:
                return {"error": "No GitHub tools available"}
            
            # Use the first GitHub tool found
            tool_name = github_tools[0]
            schema = client.get_tool_schema(tool_name)
            
            # Execute based on schema
            result = client.call_tool(
                tool_name,
                {
                    "repo": "owner/repo",
                    "action": "list_issues"
                }
            )
            
            return result
            
    except Exception as e:
        return {"error": str(e)}
```

## Key Principles

1. **Always Discover First**: Call `list_tools()` before assuming a tool exists
2. **Get Schema Before Execution**: Understand parameters before calling
3. **Handle Errors Gracefully**: Use try/except to handle MCP errors
4. **Use Context Manager**: `with` statement ensures proper cleanup
5. **Never Hallucinate Tools**: Only use tools that exist in `list_tools()` response

## Integration with Agent_Base

When creating new agents, inherit from `Agent_Base` to get MCP capability:

```python
from catalogue.Agent_Base import Agent_Base

class MyCustomAgent(Agent_Base):
    def __init__(self, agent_name: str):
        super().__init__(agent_name, role="CustomAgent")
    
    def perform_task(self):
        # Agent can use MCP tools as documented in Agent_Base docstring
        from tools.Universal_MCP_Client import create_stdio_client
        
        with create_stdio_client(["node", "mcp-server.js"]) as client:
            tools = client.list_tools()
            # ... use tools as needed
```

## System Prompt Integration

Use `generate_agent_system_prompt()` to create LLM prompts with MCP instructions:

```python
from catalogue.Agent_Base import generate_agent_system_prompt

prompt = generate_agent_system_prompt(
    agent_name="Researcher",
    role="Research Agent",
    role_specific_instructions="You specialize in finding and synthesizing information."
)

# Use this prompt when initializing the LLM agent
```

