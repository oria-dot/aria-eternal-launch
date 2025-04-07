# dispatcher_core.py – Fixed

from macroeconomic_engine import MacroeconomicEngine

def start_dispatcher():
    print("[DISPATCHER] Starting macroeconomic analysis...")
    engine = MacroeconomicEngine()
    engine.scan_global_risks()
