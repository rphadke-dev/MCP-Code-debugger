from simulation.state import SimluationState

class SimulationEngine:
    def __init__(self):
        self.state = SimluationState()

    def step_forward(self):
        self.state.step += 1

        if self.state.step == 1:
            self.state.variables['x'] = 10
            self.state.variables['z'] = 0
            self.state.call_stack = ["main"]
            self.state.last_operation = ["x = 10; z = 0"]

        elif self.state.step == 2:
            self.state.call_stack.append("divide")
            self.state.last_operation = "y = x/z"
        
        return self.state
