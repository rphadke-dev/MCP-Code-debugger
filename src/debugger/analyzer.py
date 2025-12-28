from debugger.heuristics import Heuristics
from debugger.trace import ExecutionTrace
from debugger.causal import CausalAnalyzer
from common.types import DebugReport
from simulation.history import SimulationHistory


class SimulationAnalyzer:
    def analyze(self, history: SimulationHistory) -> DebugReport:
        trace = ExecutionTrace.from_history(history)

        issues = []
        for state in trace.states:
            issues.extend(Heuristics.detect(state))

        explanations = CausalAnalyzer.explain(history)

        return DebugReport(
            total_steps=len(trace.states),
            issues=issues,
            explanations=explanations,
        )
