from simulation.state import SimluationState

class SimulationAnalyzer:
    def analyze(self, state):
        issues = {}

        if state.last_operation and "/ z" in state.last_operation:
            if state.variables.get("z") == 0:
                issues["division_by_zero"] = {
                    "severity": "high",
                    "message": "Possible division by zero detected",
                    "operation": state.last_operation,
                }

        if len(state.call_stack) > 5:
            issues["deep_call_stack"] = {
                "severity": "medium",
                "message": "Call stack unusually deep",
            }

        return issues