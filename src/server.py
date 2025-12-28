from mcp.server.fastmcp import FastMCP
from simulation.engine import SimulationEngine
from debugger.analyzer import SimulationAnalyzer

mcp = FastMCP("simulation-code-debugger")

engine = SimulationEngine()
analyzer = SimulationAnalyzer()


@mcp.tool()
def ping() -> str:
    return "pong"


@mcp.tool()
def run_simulation_step(operation: str) -> dict:
    state = engine.step(operation)
    return state.dict()


@mcp.tool()
def analyze_simulation() -> dict:
    return analyzer.analyze(engine.history)


if __name__ == "__main__":
    mcp.run()
