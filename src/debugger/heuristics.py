from simulation.state import SimulationState
from common.types import Issue


class Heuristics:
    @staticmethod
    def detect(state: SimulationState):
        issues = []

        if state.last_operation and "/" in state.last_operation:
            left, right = state.last_operation.split("/")
            if state.variables.get(right.strip()) == 0:
                issues.append(
                    Issue(
                        type="division_by_zero",
                        step=state.step,
                        message="Division by zero detected",
                        operation=state.last_operation,
                    )
                )

        return issues
