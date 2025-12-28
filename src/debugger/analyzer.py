from simulation.history import SimulationHistory
from debugger.trace import ExecutionTrace
from debugger.heuristics import Heuristics
from debugger.report import DebugReportBuilder


class SimulationAnalyzer:
    def analyze(self, history: SimulationHistory):
        trace = ExecutionTrace.from_history(history)
        heuristics = Heuristics()
        issues = heuristics.evaluate(trace)

        return DebugReportBuilder.build(
            issues=issues,
            total_steps=len(trace.states),
        )
