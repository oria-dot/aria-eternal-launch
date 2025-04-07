# aria_vanta_core_brain.py – Autonomous Self-Evolving Brain Loop (Vanta Core Layer)

from signal_memory_engine import SignalMemoryEngine
from reflex_feedback_core import ReflexFeedbackCore
from behavioral_tuner import BehavioralTuner
from strategic_reflex_loop import StrategicReflexLoop

class AriaVantaCore:
    def __init__(self, context):
        self.context = context
        self.memory = SignalMemoryEngine()
        self.feedback = ReflexFeedbackCore(self.memory)
        self.tuner = BehavioralTuner(self.memory, self.feedback)
        self.loop = StrategicReflexLoop(context)

    def run(self):
        print("Launching Vanta Core Protocol...")
        trade_result = self.loop.run()

        # Log feedback summary
        symbols = self.context.get("portfolio", {}).keys()
        tuning_report = self.tuner.get_tuning_report(symbols)
        avoid = self.tuner.build_avoid_list()
        self.context["avoid_list"] = avoid

        return {
            "trades_executed": trade_result["log"],
            "reflex_tuning": tuning_report,
            "avoid_list": avoid
        }
