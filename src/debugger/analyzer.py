from simulation.state import SimluationState

class SimulationAnalyzer:
    def analyze(self, state: SimluationState) -> dict:
        anomalies = []

        if len(state.history) >= 2:
            delta = state.history[-1] - state.history[-2]
            if delta > 1.0:
                anomalies.append({
                    "type": "RapidIncrease",
                    "description": f"Value increased by {delta} at step {state.step}"
                })
        
        trend = "increasing" if state.value > state.history[0] else "stable"

        return {
            "step": state.step,
            "current_value": state.value,
            "trend": trend,
            "anomalies": anomalies
        }