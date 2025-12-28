from mcp.server.fastmcp import FastMCP
from simulation.engine import SimulationEngine
from debugger.analyzer import SimulationAnalyzer

mcp = FastMCP("simulation-code-debugger")

engine = SimulationEngine()
analyzer = SimulationAnalyzer()


@mcp.tool()
def ping():
    return "pong"


@mcp.tool()
def run_simulation_step(operation: str):
    state = engine.run_step(operation)
    return {
        "step": state.step,
        "variables": state.variables,
        "last_operation": state.last_operation,
    }


@mcp.tool()
def analyze_simulation():
    report = analyzer.analyze(engine.history)
    return report.dict()

@mcp.tool()
def run_code(code: str):
    """
    Run a block of Python code through the simulation engine.
    """
    engine.run_code(code)
    return {
        "status": "completed",
        "steps_executed": len(engine.history.all())
    }



if __name__ == "__main__":
    mcp.run()
