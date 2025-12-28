from common.types import DebugReport
from typing import List
from common.types import Issue


class DebugReportBuilder:
    @staticmethod
    def build(issues: List[Issue], total_steps: int) -> DebugReport:
        explanations = []

        for issue in issues:
            explanations.append(
                f"Issue '{issue.type}' occurred at step {issue.step} during '{issue.operation}'"
            )

        return DebugReport(
            total_steps=total_steps,
            issues=issues,
            explanations=explanations,
        )
