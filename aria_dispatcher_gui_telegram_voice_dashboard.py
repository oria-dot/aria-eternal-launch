# ARIA Dispatcher v3 – GUI + Telegram + Voice + Dashboard (Upgraded)

import threading
import os
from dotenv import load_dotenv
from flask import Flask, jsonify

try:
    import tkinter as tk
except ImportError:
    tk = None

try:
    import pyttsx3
except ImportError:
    pyttsx3 = None

import telebot

from freelance_empire_bot import FreelanceEmpireBot
from income_core import IncomeAutomationCore
from strategy_reflex import StrategyReflexEngine

# Shared context
context = {
    "memory": [],
    "signals": {},
    "portfolio": {"AAPL": {}, "TSLA": {}},
    "status": [],
    "strategy": {},
    "income": {},
    "compliance": {},
    "emotions": [],
    "command_tree": [],
    "mode": "smart"
}

# VOICE (Cloud-safe)
def speak(msg):
    try:
        if pyttsx3:
            engine = pyttsx3.init()
            threading.Thread(target=lambda: (engine.say(msg), engine.runAndWait())).start()
        else:
            print(f"[VOICE DISABLED] {msg}")
    except Exception as e:
        print(f"[VOICE ERROR] {e}")


# FLASK DASHBOARD
app = Flask(__name__)

@app.route("/status")
def get_status():
    return jsonify({
        "status": context["status"],
        "mode": context.get("mode", "unknown"),
        "signals": context.get("signals", {})
    })

@app.route("/memory")
def get_memory():
    return jsonify({"memory": context["memory"][-10:]})

@app.route("/pnl")
def get_income():
    income = IncomeAutomationCore()
    income.add_income("Freelance", 100)
    summary = income.get_income_summary()
    return jsonify(summary)

# TELEGRAM BOT
load_dotenv()
telegram_token = os.getenv("TELEGRAM_TOKEN")
bot = telebot.TeleBot(telegram_token)

@bot.message_handler(commands=["start"])
def handle_start(message):
    bot.send_message(message.chat.id, "Aria Online. Awaiting command.")

@bot.message_handler(commands=["status"])
def handle_status(message):
    summary = f"MODE: {context['mode']}\nSTATUS: {context['status'][-3:]}"
    bot.send_message(message.chat.id, summary)

@bot.message_handler(commands=["memory"])
def handle_memory(message):
    recent = context["memory"][-5:]
    bot.send_message(message.chat.id, "\n".join(recent))

@bot.message_handler(commands=["launch_freelance"])
def handle_freelance(message):
    bot.send_message(message.chat.id, "Launching Freelance Bot...")
    result = FreelanceEmpireBot().run()
    for job in result:
        bot.send_message(message.chat.id, job)

import sys

# GUI
def launch_gui():
    if not tk:
        print("[GUI DISABLED] Tkinter is not available in this environment.")
        return

    if "RENDER" in os.environ or os.getenv("DISABLE_GUI") == "1" or "linux" in sys.platform:
        print("[GUI DISABLED] Running in headless server mode.")
        return

    root = tk.Tk()
    root.title("ARIA Dispatcher (Dashboard Mode)")
    tk.Label(root, text="ARIA v3 Command Center").pack(pady=10)

    mode_label = tk.Label(root, text="MODE: Smart")
    mode_label.pack()

    log_box = tk.Text(root, height=15, width=70)
    log_box.pack(pady=10)

    def launch_freelance_gui():
        result = FreelanceEmpireBot().run()
        for job in result:
            log_box.insert(tk.END, job + "\n")
            speak(job)

    tk.Button(root, text="Launch Freelance Income Bot", command=launch_freelance_gui).pack(pady=5)
    root.mainloop()


# Start services
import time

def run_all():
    print("[ARIA] Booting all services...")

    threading.Thread(target=bot.polling, daemon=True).start()
    threading.Thread(target=app.run, kwargs={"host": "0.0.0.0", "port": 10000}, daemon=True).start()
    launch_gui()

    # Keeps the app alive to avoid shutdown crash
    while True:
        time.sleep(10)

if __name__ == "__main__":
    run_all()
