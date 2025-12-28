# debugger/causal.py

from simulation.history import SimulationHistory
from common.types import Issue


class CausalAnalyzer:
    @staticmethod
    def explain(history: SimulationHistory, issues: list[Issue]) -> list[str]:
        explanations = []

        for issue in issues:
            if issue.type == "division_by_zero":
                explanations.append(
                    f"Variable used as divisor was set to 0 before step {issue.step}, "
                    "causing the division failure."
                )

        return explanations
