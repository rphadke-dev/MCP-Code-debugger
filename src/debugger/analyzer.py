from simulation.history import SimulationHistory
from debugger.trace import ExecutionTrace
from debugger.heuristics import Heuristics
from debugger.report import DebugReport


class SimulationAnalyzer:
    def analyze(self, history: SimulationHistory) -> dict:
        trace = ExecutionTrace.from_history(history)
        issues = Heuristics.evaluate(trace)
        return DebugReport.generate(issues)
