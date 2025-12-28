from typing import Dict, List, Any
from pydantic import BaseModel


class SimulationState(BaseModel):
    step: int = 0
    variables: Dict[str, Any] = {}
    call_stack: List[str] = []
    last_operation: str | None = None
