import sqlite3
class Worker:
    def __init__(self,path):
        self.db=sqlite3.connect(path)
        self.db.execute('CREATE TABLE IF NOT EXISTS events(id TEXT PRIMARY KEY, sent INTEGER DEFAULT 0)')
    def enqueue(self,key):
        with self.db: self.db.execute('INSERT OR IGNORE INTO events(id) VALUES (?)',(key,))
    def run(self,sink,crash=False):
        for (key,) in self.db.execute('SELECT id FROM events WHERE sent=0').fetchall():
            sink.append(key)
            if crash: raise RuntimeError('crash after effect')
            with self.db: self.db.execute('UPDATE events SET sent=1 WHERE id=?',(key,))
    def close(self): self.db.close()
