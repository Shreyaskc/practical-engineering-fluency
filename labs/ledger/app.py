import sqlite3
class Ledger:
    def __init__(self, path):
        self.db = sqlite3.connect(path)
        self.db.execute('CREATE TABLE IF NOT EXISTS shipments(id INTEGER PRIMARY KEY, key TEXT UNIQUE, qty INTEGER)')
    def create(self, key, qty):
        # BUG: retries create a new logical operation by replacing its receipt.
        with self.db:
            self.db.execute('DELETE FROM shipments WHERE key=?', (key,))
            cur = self.db.execute('INSERT INTO shipments(key,qty) VALUES (?,?)', (key,qty))
        return cur.lastrowid
    def close(self):
        self.db.close()
