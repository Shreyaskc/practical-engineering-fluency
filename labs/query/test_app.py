import sqlite3, unittest
from app import report,optimize
class Tests(unittest.TestCase):
    def test_query_budget_and_plan(self):
        db=sqlite3.connect(':memory:')
        self.addCleanup(db.close)
        db.execute('CREATE TABLE orders(id INTEGER PRIMARY KEY,tenant TEXT,status TEXT,amount INTEGER)')
        db.executemany('INSERT INTO orders VALUES (?,?,?,?)',[(1,'a','open',5),(2,'b','open',9),(3,'a','closed',7),(4,'a','open',3)])
        optimize(db); queries=[]; db.set_trace_callback(queries.append)
        self.assertEqual([(1,5),(4,3)],report(db,'a'))
        self.assertEqual(1,len(queries))
        plan=db.execute("EXPLAIN QUERY PLAN SELECT id,amount FROM orders WHERE tenant='a' AND status='open'").fetchall()
        self.assertTrue(any('SEARCH' in row[3] and 'orders_tenant_status' in row[3] for row in plan))
