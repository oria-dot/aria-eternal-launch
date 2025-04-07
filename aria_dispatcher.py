
# ARIA Central Dispatcher v1
# Connects all core intelligence, trading, business, and personality modules

from macroeconomic_engine import MacroeconomicEngine
from volatility_shield import VolatilityShield
from strategy_override_engine import StrategyOverrideEngine
from quantum_adaptive_loop import QuantumAdaptiveLoop
from freelance_empire_bot import FreelanceEmpireBot
from gumroad_autopilot import GumroadAutopilot
from portfolio_intelligence import PortfolioIntelligence
from security_guardian_phase_2 import SecurityGuardian
from self_healing_layer import SelfHealingLayer
from creative_business_generator import BusinessGenerator
from voice_persona_phase_2 import VoicePersona
from social_media_ghost_cloner import SocialMediaGhostCloner
from clone_expansion_framework import CloneExpansionFramework
from micro_saas_builder import MicroSaaSBuilder
from income_distribution_engine import IncomeDistributor
from compliance_engine import ComplianceEngine
from social_content_builder import SocialContentBuilder
from meta_command_layer import MetaCommand
from emotion_voice_layer import EmotionVoiceLayer
from aria_soul_codex import AriaSoulCodex

# Shared context object
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

# Core module orchestrator
def run_dispatcher():
    memory_engine = AriaSoulCodex()
    healing_layer = SelfHealingLayer()

    modules = [
        MacroeconomicEngine(),
        VolatilityShield(),
        StrategyOverrideEngine(),
        QuantumAdaptiveLoop(),
        FreelanceEmpireBot(),
        GumroadAutopilot(),
        PortfolioIntelligence(),
        SecurityGuardian(),
        BusinessGenerator(),
        VoicePersona(),
        SocialMediaGhostCloner(),
        CloneExpansionFramework(),
        MicroSaaSBuilder(),
        IncomeDistributor(),
        ComplianceEngine(),
        SocialContentBuilder(),
        MetaCommand(),
        EmotionVoiceLayer()
    ]

    for module in modules:
        name = module.__class__.__name__
        try:
            result = healing_layer.run_with_healing(module.run, context)
            context["memory"].append(f"{name}: {result}")
            memory_engine.store_memory(f"{name}: {result}")
        except Exception as e:
            context["status"].append(f"Failed in {name}: {e}")

    return context

if __name__ == "__main__":
    final_context = run_dispatcher()
    print("DISPATCH COMPLETE. FINAL CONTEXT SNAPSHOT:")
    print(final_context)
