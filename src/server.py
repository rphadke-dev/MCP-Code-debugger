from mcp.server.fastmcp import FastMCP
from simulation.engine import SimulationEngine
from debugger.analyzer import SimulationAnalyzer

mcp = FastMCP("simulation-debugger")

engine = SimulationEngine()
analyzer = SimulationAnalyzer()


@mcp.tool()
def run_simulation_step() -> dict:
    """
    Advance the simulation by one step and return the new state.
    """
    state = engine.step()
    return state.snapshot()


@mcp.tool()
def analyze_simulation() -> dict:
    """
    Analyze the current simulation state and explain anomalies.
    """
    return analyzer.analyze(engine.state)


@mcp.tool()
def ping() -> str:
    return "Simulation Debugger MCP is running"


if __name__ == "__main__":
    mcp.run()