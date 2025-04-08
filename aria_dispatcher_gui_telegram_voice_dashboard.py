# ARIA Dispatcher v3 – Supreme Upgrade Protocol (Unified)

import threading
import os
import sys
import time
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
from telebot import types

from freelance_empire_bot import FreelanceEmpireBot
from income_core import IncomeAutomationCore
from strategy_reflex import StrategyReflexEngine

# Shared context
context = {
    "memory": [],
    "signals": {},
    "portfolio": {"AAPL": {}, "TSLA": {}},
    "status": [],
    "strategy": {"mode": "smart", "last": "BUY AAPL"},
    "income": {"Freelance": 100},
    "compliance": {},
    "emotions": ["Stable", "Optimistic"],
    "command_tree": [],
    "mode": "smart",
    "llm_thoughts": ["Market trending up.", "Sentiment positive.", "Deploying Freelance Bot."]
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

@app.route("/memory_full")
def memory_full():
    return jsonify({"memory": context["memory"]})

@app.route("/pnl")
def get_income():
    return jsonify(context["income"])

@app.route("/trades")
def trades():
    return jsonify({"last_trade": context["strategy"].get("last", "N/A")})

@app.route("/strategy_status")
def strategy_status():
    return jsonify(context["strategy"])

@app.route("/llm_brain")
def llm_brain():
    return jsonify({"thoughts": context["llm_thoughts"]})

@app.route("/emotions")
def emotions():
    return jsonify({"emotions": context.get("emotions", [])})

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

@bot.message_handler(commands=["speak"])
def handle_speak(message):
    msg = message.text.replace("/speak", "").strip()
    if msg:
        speak(msg)
        bot.send_message(message.chat.id, f"Speaking: {msg}")

@bot.message_handler(commands=["mute"])
def handle_mute(message):
    global pyttsx3
    pyttsx3 = None
    bot.send_message(message.chat.id, "🔇 Voice has been disabled.")

@bot.message_handler(commands=["strategy_status"])
def handle_strategy(message):
    summary = context.get("strategy", {})
    bot.send_message(message.chat.id, f"Strategy Mode: {summary.get('mode')}\nLast Signal: {summary.get('last')}")

@bot.message_handler(commands=["income_summary"])
def handle_income(message):
    income = context.get("income", {})
    summary = "\n".join([f"{k}: ${v}" for k, v in income.items()])
    bot.send_message(message.chat.id, f"💰 Income Summary:\n{summary}")

@bot.message_handler(commands=["reset_memory"])
def reset_memory(message):
    context["memory"] = []
    bot.send_message(message.chat.id, "🧠 Memory wiped clean.")

@bot.message_handler(func=lambda msg: msg.text and msg.text.lower() == "hi aria")
def handle_hi_aria(message):
    memory_count = len(context.get("memory", []))
    signals_count = len(context.get("signals", {}))
    portfolio = ', '.join(context.get("portfolio", {}).keys())
    mode = context.get("mode", "unknown")

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("/status", "/memory", "/pnl")
    markup.row("/launch_freelance", "/strategy_status")
    markup.row("/help", "/reset_memory")

    summary = f"""🧠 Good day, Commander.

✨ ARIA Operational Brief:
- Mode: {mode}
- Memory Logs: {memory_count}
- Signals Tracked: {signals_count}
- Portfolio: {portfolio or 'None'}
- Freelance Bot: ✅ Ready

Use /help to see all available commands.
"""
    bot.send_message(message.chat.id, summary, reply_markup=markup)

@bot.message_handler(commands=["help"])
def handle_help(message):
    commands = [
        "/start — Boot ARIA",
        "/status — System status",
        "/memory — Show memory logs",
        "/pnl — Income summary",
        "/dashboard — Link to live dashboard",
        "/launch_freelance — Deploy income bot",
        "/income_summary — Show income",
        "/strategy_status — AI trading info",
        "/speak <msg> — Voice response",
        "/mute — Disable voice",
        "/reset_memory — Wipe memory",
        "/hi aria — Quick summary"
    ]
    bot.send_message(message.chat.id, "🧭 Available Commands:\n" + "\n".join(commands))

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
