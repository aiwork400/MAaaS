# Tools Package Initialization
# ----------------------------
# This file allows the 'tools' folder to be treated as a Python package.

# We attempt to import the full MCP Client if available, but wrap it in a try/except block.
# This prevents the entire package from crashing if Universal_MCP_Client is missing
# or has dependency issues, allowing standalone tools (like mcp_market_scanner) to still work.

try:
    from .Universal_MCP_Client import (
        UniversalMCPClient,
        TransportType,
        MCPError,
        MCPConnectionError,
        MCPExecutionError,
        MCPTimeoutError,
        create_stdio_client,
        create_sse_client
    )
    __all__ = [
        "UniversalMCPClient",
        "TransportType",
        "MCPError",
        "MCPConnectionError",
        "MCPExecutionError",
        "MCPTimeoutError",
        "create_stdio_client",
        "create_sse_client"
    ]
except ImportError:
    # If the complex client fails, we fail silently so other tools still load.
    pass