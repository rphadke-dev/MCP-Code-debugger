from simulation.history import SimulationHistory
from simulation.state import SimulationState
from typing import List


class ExecutionTrace:
    def __init__(self, states: List[SimulationState]):
        self.states = states

    @classmethod
    def from_history(cls, history: SimulationHistory) -> "ExecutionTrace":
        return cls(history.all())
