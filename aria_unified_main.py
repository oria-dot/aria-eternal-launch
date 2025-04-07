load_env()
#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
ARIA UNIFIED MAIN SYSTEM
Fully integrated, single-file execution of the Overwatch Protocol
Upgraded: Async Dispatcher + Timers + Logger + Config Flexibility
"""

import os
from aria_core.env_loader import load_env
import sys
import asyncio
import time

from loguru import logger
import yaml
from aria_core.config_loader import load_and_validate_config
CONFIG_PATH = os.getenv("ARIA_CONFIG_PATH", "config/aria_config.yaml")

def load_and_validate_config():
    if os.path.exists(CONFIG_PATH):
        with open(CONFIG_PATH, "r") as f:
            return yaml.safe_load(f)
    return {}

from datetime import datetime

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

# Set up logging
logger.add('logs/aria_runtime.log', rotation='500 KB', retention='10 days', level='INFO')(filename='aria_dispatcher.log', level=logging.INFO,
                    format='%(asctime)s [%(levelname)s] %(message)s')

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

# Async module runner with timer and logging
async def run_dispatcher():
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
        start_time = time.time()
        try:
            result = healing_layer.run_with_healing(module.run, context)
            context["memory"].append(f"{name}: {result}")
            memory_engine.store_memory(f"{name}: {result}")
            elapsed = round(time.time() - start_time, 2)
            logging.info(f"{name} executed in {elapsed}s: {result}")
        except Exception as e:
            error_msg = f"Failed in {name}: {e}"
            context["status"].append(error_msg)
            logging.error(error_msg)

    return context

# Execution entry point
if __name__ == "__main__":
    asyncio.run(run_dispatcher())


async def main():
    logger.info("Starting ARIA Unified Main")
    config = load_and_validate_config()
    start = time.time()
    try:
        # Simulate dispatcher
        logger.info("Dispatching modules...")
        await asyncio.sleep(2)  # placeholder for real run
        logger.success("Modules dispatched successfully.")
    except Exception as e:
        logger.exception(f"Critical error during ARIA run: {e}")
    finally:
        elapsed = round(time.time() - start, 2)
        logger.info(f"ARIA finished in {elapsed}s")

if __name__ == "__main__":
    asyncio.run(main())
