from typing import List
from debugger.trace import ExecutionTrace
from common.types import Issue


class Heuristics:
    @staticmethod
    def evaluate(trace: ExecutionTrace) -> List[Issue]:
        issues: List[Issue] = []

        for step in trace.steps:
            if step.last_operation and "/0" in step.last_operation.replace(" ", ""):
                issues.append(
                    Issue(
                        id="division_by_zero",
                        severity="high",
                        message="Possible division by zero detected",
                        step=step.step,
                        operation=step.last_operation,
                    )
                )

            if len(step.call_stack) > 5:
                issues.append(
                    Issue(
                        id="deep_call_stack",
                        severity="medium",
                        message="Call stack unusually deep",
                        step=step.step,
                    )
                )

        return issues
