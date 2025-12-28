from typing import List
from pydantic import BaseModel


class Issue(BaseModel):
    type: str
    step: int
    message: str
    operation: str


class DebugReport(BaseModel):
    total_steps: int
    issues: List[Issue]
    explanations: List[str]
    suggestions: List[Suggestion]

class Suggestion(BaseModel):
    issue_type: str
    message: str
    example_fix: str
