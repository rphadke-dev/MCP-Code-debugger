from pydantic import BaseModel
from typing import List

class SimluationState(BaseModel):
    step: int
    value: float
    history: List[float]

    def snapshot(self) -> dict:
        return {
            "step": self.step,
            "value": self.value,
            "history": self.history.copy()
        }