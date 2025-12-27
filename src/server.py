from mcp.server.fastmcp import FastMCP

mcp = FastMCP(
    name = "simulation-code-debugger"
)

@mcp.tool()
def ping() -> str:
    """
    Health check tool
    """
    return "Simualtion debugger MCP is running"

if __name__ == "__main__":
    mcp.run()
