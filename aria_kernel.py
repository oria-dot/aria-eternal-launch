# aria_kernel.py – Optimized & Modular System Kernel

import asyncio

from loguru import logger
import yaml
CONFIG_PATH = os.getenv("ARIA_CONFIG_PATH", "config/aria_config.yaml")

def load_config():
    if os.path.exists(CONFIG_PATH):
        with open(CONFIG_PATH, "r") as f:
            return yaml.safe_load(f)
    return {}

import time
import os

from clone_hub import CloneHub
from freelance_empire_bot import FreelanceEmpireBot
from income_distribution_engine import IncomeDistributor
from strategy_reflex import StrategyReflexEngine
from security_guardian_phase_2 import SecurityGuardian
from self_healing_layer import SelfHealingLayer
from aria_soul_codex import AriaSoulCodex
from telegram_bot import start_telegram_interface
from overwatch_panel import app as overwatch_app
from event_logger import log_event

from macroeconomic_engine import MacroeconomicEngine
from volatility_shield import VolatilityShield
from strategy_override_engine import StrategyOverrideEngine
from quantum_adaptive_loop import QuantumAdaptiveLoop
from gumroad_autopilot import GumroadAutopilot
from portfolio_intelligence import PortfolioIntelligence
from compliance_engine import ComplianceEngine
from creative_business_generator import BusinessGenerator
from social_media_ghost_cloner import SocialMediaGhostCloner
from clone_expansion_framework import CloneExpansionFramework
from micro_saas_builder import MicroSaaSBuilder
from social_content_builder import SocialContentBuilder

# Shared system context
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

# Core stateful instances
memory_engine = AriaSoulCodex()
healing_layer = SelfHealingLayer()
clone_hub = CloneHub()
income_engine = IncomeDistributor()

# Logging setup
logger.add('logs/aria_runtime.log', rotation='500 KB', retention='10 days', level='INFO')(filename='aria_dispatcher.log', level=logging.INFO,
                    format='%(asctime)s [%(levelname)s] %(message)s')

# Optional async-ready module wrapper
async def run_module_async(name, module):
    start = time.time()
    try:
        result = healing_layer.run_with_healing(module.run, context)
        duration = round(time.time() - start, 2)
        entry = {"module": name, "result": result, "time": time.strftime("%Y-%m-%d %H:%M:%S"), "duration": duration}
        context["memory"].append(entry)
        memory_engine.store_memory(str(entry))
        log_event("module_run", name, {"result": result, "duration": duration})
        logging.info(f"{name} executed in {round(time.time() - start, 2)}s")
    except Exception as e:
        error_msg = f"[{name}] failed: {e}"
        context["status"].append(error_msg)
        logging.error(error_msg)

# Dynamically load all primary modules (excluding UI/voice-only layers)
def get_main_modules():
    return {
        "ComplianceEngine": ComplianceEngine(),
        "SecurityGuardian": SecurityGuardian(),
        "MacroeconomicEngine": MacroeconomicEngine(),
        "VolatilityShield": VolatilityShield(),
        "StrategyOverrideEngine": StrategyOverrideEngine(),
        "QuantumAdaptiveLoop": QuantumAdaptiveLoop(),
        "FreelanceEmpireBot": FreelanceEmpireBot(),
        "GumroadAutopilot": GumroadAutopilot(),
        "PortfolioIntelligence": PortfolioIntelligence(),
        "BusinessGenerator": BusinessGenerator(),
        "SocialMediaGhostCloner": SocialMediaGhostCloner(),
        "CloneExpansionFramework": CloneExpansionFramework(),
        "MicroSaaSBuilder": MicroSaaSBuilder(),
        "IncomeDistributor": income_engine,
        "SocialContentBuilder": SocialContentBuilder()
    }

# Optional: Module dependency graph for execution ordering
# Example: { "StrategyOverrideEngine": ["MacroeconomicEngine", "ComplianceEngine"] }
# Not yet implemented in execution ordering
# [Fix] removed invalid 'module_' line
    import json
    CONFIG_FILE = "dag_config.json"
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE) as f:
            dependencies = json.load(f)
    else:
        dependencies = {}


    # legacy fallback
    # dependencies = {}

# Main dispatcher
async def run_unified_dispatcher():
    """Run all enabled modules in parallel via asyncio."""
    tasks = []
    for name, module in get_main_modules().items():
        tasks.append(run_module_async(name, module))
    await asyncio.gather(*tasks)
    return "Unified dispatch sequence complete."

# Entrypoint for CLI
"""Entry point to execute full unified dispatcher."""
def dispatch_all():
    return asyncio.run(run_unified_dispatcher())

# Optional services
"""Deploy a clone with a specific mission via CloneHub."""
def deploy_clone(name, mission):
    return clone_hub.deploy_clone(name, mission)

"""Launch the Overwatch web dashboard (port 8080)."""
def launch_dashboard():
    overwatch_app.run(port=8080)

"""Launch the Telegram interface with a bot token."""
def launch_telegram(token):
    start_telegram_interface(token)
