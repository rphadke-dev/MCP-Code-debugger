from typing import List, Dict, Any
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
