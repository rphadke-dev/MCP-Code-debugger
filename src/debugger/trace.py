from typing import List
from simulation.history import SimulationHistory
from common.types import TraceStep


class ExecutionTrace:
    def __init__(self, steps: List[TraceStep]):
        self.steps = steps

    @classmethod
    def from_history(cls, history: SimulationHistory) -> "ExecutionTrace":
        steps = [
            TraceStep(
                step=s.step,
                variables=s.variables,
                call_stack=s.call_stack,
                last_operation=s.last_operation,
            )
            for s in history.all()
        ]
        return cls(steps)
