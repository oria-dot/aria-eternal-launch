# aria_main.py – Unified Modular Launcher

from aria_core.dispatcher.dispatcher_core import DispatcherCore
from aria_core.context.context import AriaContext
from aria_core.memory.memory_core import MemoryEngine
from aria_core.gui.dashboard_launcher import launch_dashboard
from aria_core.voice.voice_manager import VoiceManager
from telegram_bot import start_telegram_interface

def main():
    context = AriaContext.get()
    memory = MemoryEngine(context)
    voice = VoiceManager()

    dispatcher = DispatcherCore(context, memory, voice)
    dispatcher.run_all_modules()

    # Optional Interfaces
    launch_dashboard(context)
    start_telegram_interface(context)

if __name__ == "__main__":
    main()
