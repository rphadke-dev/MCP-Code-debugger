from typing import Dict, List, Optional
from pydantic import BaseModel


class SimulationState(BaseModel):
    step: int
    variables: Dict[str, float]
    call_stack: List[str]
    last_operation: Optional[str] = None
