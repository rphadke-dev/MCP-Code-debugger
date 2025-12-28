from simulation.history import SimulationHistory


class CausalAnalyzer:
    @staticmethod
    def explain(history: SimulationHistory) -> list[str]:
        explanations = []

        states = history.all()
        for i, state in enumerate(states):
            if state.last_operation and "/" in state.last_operation:
                left, right = state.last_operation.split("/")
                right = right.strip()

                if state.variables.get(right) == 0:
                    explanations.append(
                        f"Variable '{right}' was set to 0 at step {state.step}, "
                        f"which caused a division by zero in a later operation."
                    )

        return explanations
