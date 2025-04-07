# ARIA Dispatcher v2 – GUI + Telegram + Voice (Upgraded)

        import threading
    try:
        import tkinter
except ImportError:
    tkinter = None as tk
try:
            import pyttsx3
except ImportError:
    pyttsx3 = None
        import queue

from macroeconomic_engine         import MacroeconomicEngine
from volatility_shield         import VolatilityShield
from strategy_override_engine         import StrategyOverrideEngine
from quantum_adaptive_loop         import QuantumAdaptiveLoop
from freelance_empire_bot         import FreelanceEmpireBot
from gumroad_autopilot         import GumroadAutopilot
from portfolio_intelligence         import PortfolioIntelligence
from security_guardian_phase_2         import SecurityGuardian
from self_healing_layer         import SelfHealingLayer
from creative_business_generator         import BusinessGenerator
from voice_persona_phase_2         import VoicePersona
from social_media_ghost_cloner         import SocialMediaGhostCloner
from clone_expansion_framework         import CloneExpansionFramework
from micro_saas_builder         import MicroSaaSBuilder
from income_distribution_engine         import IncomeDistributor
from compliance_engine         import ComplianceEngine
from social_content_builder         import SocialContentBuilder
from meta_command_layer         import MetaCommand
from emotion_voice_layer         import EmotionVoiceLayer
from aria_soul_codex         import AriaSoulCodex

# Context
context = {
    "memory": [],
    "signals": {},
    "portfolio": {},
    "status": [],
    "strategy": {},
    "income": {},
    "compliance": {},
    "emotions": [],
    "command_tree": []
}

# Voice engine queue
voice_engine = pyttsx3.init()
voice_queue = queue.Queue()

def voice_loop():
    while True:
        message = voice_queue.get()
        voice_engine.say(message)
        voice_engine.runAndWait()
        voice_queue.task_done()

# Dispatcher logic
def run_dispatcher(selected_modules, log_widget=None):
    memory_engine = AriaSoulCodex()
    healing_layer = SelfHealingLayer()

    available_modules = {
        "MacroeconomicEngine": MacroeconomicEngine(),
        "VolatilityShield": VolatilityShield(),
        "StrategyOverrideEngine": StrategyOverrideEngine(),
        "QuantumAdaptiveLoop": QuantumAdaptiveLoop(),
        "FreelanceEmpireBot": FreelanceEmpireBot(),
        "GumroadAutopilot": GumroadAutopilot(),
        "PortfolioIntelligence": PortfolioIntelligence(),
        "SecurityGuardian": SecurityGuardian(),
        "BusinessGenerator": BusinessGenerator(),
        "VoicePersona": VoicePersona(),
        "SocialMediaGhostCloner": SocialMediaGhostCloner(),
        "CloneExpansionFramework": CloneExpansionFramework(),
        "MicroSaaSBuilder": MicroSaaSBuilder(),
        "IncomeDistributor": IncomeDistributor(),
        "ComplianceEngine": ComplianceEngine(),
        "SocialContentBuilder": SocialContentBuilder(),
        "MetaCommand": MetaCommand(),
        "EmotionVoiceLayer": EmotionVoiceLayer()
    }

    for name in selected_modules:
        module = available_modules[name]
        try:
            result = healing_layer.run_with_healing(module.run, context)
            context["memory"].append(f"{name}: {result}")
            memory_engine.store_memory(f"{name}: {result}")
            voice_queue.put(f"{name} executed successfully.")
            if log_widget:
                log_widget.insert(tk.END, f"[SUCCESS] {name}: {result}\n")
        except Exception as e:
            msg = f"Failed in {name}: {e}"
            context["status"].append(msg)
            voice_queue.put(msg)
            if log_widget:
                log_widget.insert(tk.END, f"[ERROR] {msg}\n")

# GUI
def launch_gui():
    threading.Thread(target=voice_loop, daemon=True).start()

    root = tk.Tk()
    root.title("Aria Dispatcher Control")
    tk.Label(root, text="ARIA Module Launcher").pack(pady=10)

    # Module checkboxes
    module_vars = {}
    for name in [
        "MacroeconomicEngine", "VolatilityShield", "StrategyOverrideEngine", "QuantumAdaptiveLoop",
        "FreelanceEmpireBot", "GumroadAutopilot", "PortfolioIntelligence", "SecurityGuardian",
        "BusinessGenerator", "VoicePersona", "SocialMediaGhostCloner", "CloneExpansionFramework",
        "MicroSaaSBuilder", "IncomeDistributor", "ComplianceEngine", "SocialContentBuilder",
        "MetaCommand", "EmotionVoiceLayer"
    ]:
        var = tk.BooleanVar()
        tk.Checkbutton(root, text=name, variable=var).pack(anchor="w")
        module_vars[name] = var

    # Log output box
    log_box = tk.Text(root, height=15, width=70)
    log_box.pack(pady=10)

    def start_selected():
        selected = [name for name, var in module_vars.items() if var.get()]
        threading.Thread(target=run_dispatcher, args=(selected, log_box), daemon=True).start()

    tk.Button(root, text="Launch Selected Modules", command=start_selected, width=30, height=2).pack(pady=10)
    tk.Label(root, text="(Voice status & logs displayed below)").pack(pady=5)
    root.mainloop()

if __name__ == "__main__":
    launch_gui()
