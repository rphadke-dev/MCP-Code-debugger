from simulation.state import SimulationState
from simulation.history import SimulationHistory


class SimulationEngine:
    def __init__(self):
        self.state = SimulationState()
        self.history = SimulationHistory()

    def step(self, operation: str) -> SimulationState:
        self.state.step += 1
        self.state.last_operation = operation

        # NOTE: We do NOT evaluate expressions yet (Day 5)
        # We only record intent
        self.history.add(self.state.copy())

        return self.state

    def reset(self):
        self.state = SimulationState()
        self.history.clear()
