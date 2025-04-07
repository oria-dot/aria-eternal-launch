import sqlite3
from datetime import datetime

DB_FILE = "clone_memory.db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS memory (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            clone TEXT NOT NULL,
            mission TEXT NOT NULL,
            result TEXT,
            timestamp TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def save_memory(clone, mission, result):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("INSERT INTO memory (clone, mission, result, timestamp) VALUES (?, ?, ?, ?)", 
              (clone, mission, result, datetime.now().isoformat()))
    conn.commit()
    conn.close()

def get_memory(clone):
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("SELECT mission, result, timestamp FROM memory WHERE clone = ? ORDER BY id DESC LIMIT 20", (clone,))
    rows = c.fetchall()
    conn.close()
    return rows