from common.types import Issue
from debugger.trace import ExecutionTrace


class Heuristics:
    def evaluate(self, trace: ExecutionTrace):
        issues = []

        for state in trace.states:
            if state.last_operation and "/" in state.last_operation:
                parts = state.last_operation.split()
                if len(parts) == 3:
                    _, _, right = parts
                    if state.variables.get(right) == 0:
                        issues.append(
                            Issue(
                                type="division_by_zero",
                                step=state.step,
                                message="Division by zero detected",
                                operation=state.last_operation,
                            )
                        )

        return issues
