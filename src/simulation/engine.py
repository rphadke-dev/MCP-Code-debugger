from simulation.state import SimluationState

class SimulationEngine:
    def __init__(self):
        self.state = SimluationState(
            step=0,
            value=1.0,
            history=[1.0]
        )

    def step(self) -> SimluationState:

        self.state.step += 1

        # Simple non-linear behavior
        delta = (self.state.step % 3) * 0.5
        self.state.value += delta

        self.state.history.append(self.state.value)
        return self.state 