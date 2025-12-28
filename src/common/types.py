from typing import Dict, Any, List
from pydantic import BaseModel


class Issue(BaseModel):
    id: str
    severity: str
    message: str
    step: int | None = None
    operation: str | None = None


class TraceStep(BaseModel):
    step: int
    variables: Dict[str, Any]
    call_stack: List[str]
    last_operation: str | None
