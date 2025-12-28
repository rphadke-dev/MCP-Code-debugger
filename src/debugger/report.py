from typing import List
from simulation.state import SimulationState
from common.types import DebugReport, Issue


class ReportBuilder:
    @staticmethod
    def generate(states: List[SimulationState]) -> DebugReport:
        explanations = []

        for state in states:
            for var, val in state.variables.items():
                if val == 0:
                    explanations.append(
                        f"Variable '{var}' was set to 0 at step {state.step}."
                    )

        return DebugReport(
            total_steps=len(states),
            issues=[],
            explanations=explanations,
            suggestions=[],
        )
