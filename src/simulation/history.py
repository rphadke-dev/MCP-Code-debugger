from typing import List
from simulation.state import SimulationState


class SimulationHistory:
    def __init__(self):
        self._states: List[SimulationState] = []

    def add(self, state: SimulationState):
        self._states.append(state)

    def all(self) -> List[SimulationState]:
        return self._states

    def clear(self):
        self._states.clear()
