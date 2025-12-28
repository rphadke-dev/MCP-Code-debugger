from typing import List
from simulation.state import SimulationState


class SimulationHistory:
    def __init__(self):
        self._states: List[SimulationState] = []

    def append(self, state: SimulationState):
        self._states.append(state)

    def all(self) -> List[SimulationState]:
        return list(self._states)

    def clear(self):
        self._states.clear()
