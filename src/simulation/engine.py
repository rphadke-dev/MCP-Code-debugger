import operator as py_operator
from simulation.state import SimulationState
from simulation.history import SimulationHistory


BINARY_OPS = {
    "+": py_operator.add,
    "-": py_operator.sub,
    "*": py_operator.mul,
    "/": py_operator.truediv,
}


class SimulationEngine:
    def __init__(self):
        self.history = SimulationHistory()
        self.variables = {}
        self.step = 0

    def run_step(self, operation: str) -> SimulationState:
        self.step += 1
        operation = operation.strip()

        try:
            # Assignment: x = 10
            if "=" in operation and not any(op in operation for op in BINARY_OPS):
                var, value = operation.split("=")
                self.variables[var.strip()] = float(value.strip())

            # Binary operation: x / y
            else:
                left, op, right = operation.split()

                if op not in BINARY_OPS:
                    raise ValueError(f"Unsupported operator: {op}")

                if left not in self.variables or right not in self.variables:
                    raise ValueError("Undefined variable used in operation")

                result = BINARY_OPS[op](
                    self.variables[left],
                    self.variables[right],
                )
                self.variables[left] = result

        except Exception:
            state = SimulationState(
                step=self.step,
                variables=self.variables.copy(),
                call_stack=[],
                last_operation=operation,
            )
            self.history.append(state)
            raise

        state = SimulationState(
            step=self.step,
            variables=self.variables.copy(),
            call_stack=[],
            last_operation=operation,
        )
        self.history.append(state)
        return state
