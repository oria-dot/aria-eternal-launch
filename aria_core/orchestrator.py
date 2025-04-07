import asyncio
import importlib
from loguru import logger
from pathlib import Path
import time

MODULES = {
    "TradingEngine": "aria_core.ai_intelligence_core.auto_trading_intelligence_3_0",
    "PortfolioOptimizer": "aria_core.ai_intelligence_core.portfolio_intelligence",
    "StrategyReflex": "aria_core.trader.strategy_reflex",
    "IncomeRedistributor": "income_distribution_engine",
    "CloneFarm": "aria_core.ai_intelligence_core.clone_farm",
    "ComplianceModule": "compliance_engine"
}

async def run_module(name, path):
    try:
        mod = importlib.import_module(path)
        if hasattr(mod, "run"):
            logger.info(f"[{name}] running...")
            await asyncio.to_thread(mod.run)
        else:
            logger.warning(f"[{name}] has no 'run' function")
    except Exception as e:
        logger.error(f"[{name}] crashed: {e}")

async def orchestrate():
    while True:
        tasks = [run_module(name, path) for name, path in MODULES.items()]
        await asyncio.gather(*tasks)
        logger.info("Cycle complete. Sleeping 30s.")
        await asyncio.sleep(30)

if __name__ == "__main__":
    logger.info("Starting ARIA Orchestrator")
    asyncio.run(orchestrate())