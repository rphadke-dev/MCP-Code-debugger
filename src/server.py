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
def run_simulation_step():
    state = engine.step_forward()
    return {
        "step": state.step,
        "variables": state.variables,
        "call_stack": state.call_stack,
        "last_operation": state.last_operation,
        "issues": state.issues,
    }

@mcp.tool()
def analyze_simulation():
    issues = analyzer.analyze(engine.state)
    engine.state.issues = issues
    return issues

if __name__ == "__main__":
    mcp.run()