from simulation.history import SimulationHistory


class CausalAnalyzer:
    @staticmethod
    def explain(history: SimulationHistory):
        explanations = []
        states = history.all()

        for i in range(1, len(states)):
            prev = states[i - 1]
            curr = states[i]

            for var, value in curr.variables.items():
                if var in prev.variables and value == 0:
                    explanations.append(
                        f"Variable '{var}' was set to 0 at step {curr.step}, "
                        f"which likely caused a later failure."
                    )

        return explanations
