from common.types import Suggestion

class SuggestionEngine:
    @staticmethod
    def suggest(issue):
        if issue.type == "division_by_zero":
            return Suggestion(
                issue_type="division_by_zero",
                message="Guard against zero before division",
                example_fix="if y != 0:\n    x / y"
            )
        return None
