from typing import List
from common.types import Issue


class FixSuggestion:
    @staticmethod
    def suggest(issue: Issue) -> List[str]:
        if issue.type == "division_by_zero":
            return [
                f"Add a guard before '{issue.operation}' (e.g. `if y != 0:`).",
                "Validate divisor values before division.",
            ]

        return ["Review this operation for potential issues."]
