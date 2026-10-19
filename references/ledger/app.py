import sqlite3
class Ledger:
    def __init__(self, path):
        self.db = sqlite3.connect(path)
        self.db.execute('CREATE TABLE IF NOT EXISTS shipments(id INTEGER PRIMARY KEY, key TEXT UNIQUE, qty INTEGER)')
    def create(self, key, qty):
        if not isinstance(key,str) or not key.strip() or type(qty) is not int or qty <= 0:
            raise ValueError('invalid shipment')
        with self.db:
            self.db.execute('INSERT OR IGNORE INTO shipments(key,qty) VALUES (?,?)', (key,qty))
            receipt, old_qty = self.db.execute('SELECT id,qty FROM shipments WHERE key=?',(key,)).fetchone()
            if old_qty != qty: raise ValueError('key conflict')
            return receipt
    def close(self): self.db.close()
