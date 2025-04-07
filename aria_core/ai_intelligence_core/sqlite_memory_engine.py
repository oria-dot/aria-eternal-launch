
import sqlite3

class SQLiteMemoryEngine:
    def __init__(self, db_path="aria_memory.db"):
        self.db_path = db_path
        self.conn = sqlite3.connect(self.db_path)
        self.cursor = self.conn.cursor()
        self._initialize_db()

    def _initialize_db(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS memory (
                                id INTEGER PRIMARY KEY, 
                                module TEXT, 
                                action TEXT, 
                                outcome TEXT, 
                                timestamp TEXT)''')
        self.conn.commit()

    def save(self, module, action, outcome, timestamp):
        self.cursor.execute('''INSERT INTO memory (module, action, outcome, timestamp) 
                               VALUES (?, ?, ?, ?)''', (module, action, outcome, timestamp))
        self.conn.commit()

    def query_recent(self, limit=10):
        self.cursor.execute(f"SELECT * FROM memory ORDER BY timestamp DESC LIMIT {limit}")
        return self.cursor.fetchall()
