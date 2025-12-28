from typing import List
from common.types import Issue


class DebugReport:
    @staticmethod
    def generate(issues: List[Issue]) -> dict:
        return {
            "issues": [issue.dict() for issue in issues],
            "total_issues": len(issues),
            "explanations": [issue.message for issue in issues],
        }
