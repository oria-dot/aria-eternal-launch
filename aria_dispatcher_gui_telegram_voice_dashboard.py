# ARIA Dispatcher v4 – Ascension Tier II (Clone Sync + Reflex AI + Signal Receiver + Compliance Core)

import threading
import os
import sys
import time
from dotenv import load_dotenv
from flask import Flask, jsonify, send_file, request
import io

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
from reportlab.pdfgen import canvas

# Shared context
context = {
    "memory": [],
    "signals": {},
    "portfolio": {"AAPL": {}, "TSLA": {}},
    "status": [],
    "strategy": {"mode": "smart", "last": "BUY AAPL"},
    "income": {"Freelance": 100, "Payments": []},
    "compliance": {"logs": []},
    "emotions": ["Stable", "Optimistic"],
    "command_tree": [],
    "mode": "smart",
    "llm_thoughts": ["Market trending up.", "Sentiment positive.", "Deploying Freelance Bot."],
    "clones": [],
    "payment_links": {
        "PayPal": "https://paypal.me/AgbelGjedia",
        "Bitcoin": "bc1qk4yc86ch79wnw2zzm6d74qxsfqauy83ayf6w3c",
        "Ethereum": "0x6017A98aDd3616dCe00BccE89c5D2a6A31343f26",
        "USDT": "TY5JAvFp8ZPxAyVfgLsJwzuDqW4tY3Zp7R",
        "Solana": "4RM8M2L2EDSiDhGEVKy3mnfyQEpJwYBqkM5uF4gM7cSe",
        "BNB": "bnb1d2yeezxk7q82pqdtvx8t0y79lj9dpd99csj5qp",
        "XRP": "rEb8TK3gBgk5auZkwc6sHnwrGVJH8DuaLh",
        "USDC": "0x8f77842D6E0151e86b946FE90D2615B596D8935C"
    }
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

@app.route("/payments")
def get_payments():
    return jsonify({"payments": context["income"].get("Payments", [])})

@app.route("/clone_report", methods=["POST"])
def clone_report():
    data = request.json
    context["clones"].append(data)
    return jsonify({"msg": "Clone status received."})

@app.route("/compliance")
def compliance():
    return jsonify({"logs": context["compliance"].get("logs", [])})

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
        if any(x in job for x in ["(BTC)", "(ETH)", "(PayPal)"]):
            context["income"]["Payments"].append({"job": job, "status": "applied"})
        bot.send_message(message.chat.id, job)

@bot.message_handler(commands=["clear_payments"])
def clear_payments(message):
    context["income"]["Payments"] = []
    bot.send_message(message.chat.id, "🧹 Payments log has been cleared.")

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
    summary = "\n".join([f"{k}: ${v}" if k != "Payments" else f"Payments: {len(v)} txns" for k, v in income.items()])
    bot.send_message(message.chat.id, f"💰 Income Summary:\n{summary}")

@bot.message_handler(commands=["reset_memory"])
def reset_memory(message):
    context["memory"] = []
    bot.send_message(message.chat.id, "🧠 Memory wiped clean.")

@bot.message_handler(commands=["receipt"])
def handle_receipt(message):
    parts = message.text.split(" ", 1)
    if len(parts) < 2:
        bot.send_message(message.chat.id, "⚠️ Usage: /receipt <job name>")
        return
    job_name = parts[1]
    buffer = io.BytesIO()
    pdf = canvas.Canvas(buffer)
    pdf.drawString(100, 750, "ARIA INCOME RECEIPT")
    pdf.drawString(100, 730, f"Job: {job_name}")
    pdf.drawString(100, 710, f"Status: Generated by ARIA AI")
    pdf.save()
    buffer.seek(0)
    bot.send_document(message.chat.id, buffer, visible_file_name="receipt.pdf")

@bot.message_handler(func=lambda msg: msg.text and msg.text.lower() == "hi aria")
def handle_hi_aria(message):
    memory_count = len(context.get("memory", []))
    signals_count = len(context.get("signals", {}))
    portfolio = ', '.join(context.get("portfolio", {}).keys())
    mode = context.get("mode", "unknown")
    pay = context.get("payment_links", {})

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row("/status", "/memory", "/pnl")
    markup.row("/launch_freelance", "/strategy_status")
    markup.row("/clear_payments", "/reset_memory", "/receipt")

    summary = f"""🧠 Good day, Commander.

✨ ARIA Operational Brief:
- Mode: {mode}
- Memory Logs: {memory_count}
- Signals Tracked: {signals_count}
- Portfolio: {portfolio or 'None'}
- Freelance Bot: ✅ Ready

💳 Payment Links:
- PayPal: {pay['PayPal']}
- BTC: {pay['Bitcoin']}
- ETH: {pay['Ethereum']}

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
        "/clear_payments — Clear payment logs",
        "/receipt <job> — Download receipt",
        "/hi aria — Quick summary"
    ]
    bot.send_message(message.chat.id, "🧭 Available Commands:\n" + "\n".join(commands))

# Auto Scanner (Background Freelance Monitor)
def auto_scan_freelance():
    while True:
        print("[Auto-Scanner] Checking freelance opportunities...")
        jobs = FreelanceEmpireBot().run()
        for job in jobs:
            if any(x in job for x in ["(BTC)", "(ETH)", "(PayPal)"]):
                context["income"]["Payments"].append({"job": job, "status": "auto-applied"})
                context["memory"].append(f"Auto-applied to: {job}")
        time.sleep(900)

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
    tk.Label(root, text="ARIA v4 Command Center").pack(pady=10)

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
    threading.Thread(target=auto_scan_freelance, daemon=True).start()
    launch_gui()

    while True:
        time.sleep(10)

if __name__ == "__main__":
    run_all()

