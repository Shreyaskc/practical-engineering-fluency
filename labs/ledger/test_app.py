import unittest, tempfile
from pathlib import Path
from app import Ledger
class Tests(unittest.TestCase):
    def test_retry_and_restart(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'db'; a=Ledger(p)
            first=a.create('req-1',2); a.create('other',1)
            self.assertEqual(first,a.create('req-1',2)); a.close()
            b=Ledger(p)
            self.assertEqual(first,b.create('req-1',2))
            self.assertEqual(2,b.db.execute('SELECT count(*) FROM shipments').fetchone()[0]); b.close()
    def test_conflict_and_validation(self):
        a=Ledger(':memory:')
        try:
            a.create('k',2)
            with self.assertRaises(ValueError): a.create('k',3)
            for key,qty in [('',1),('x',0),('x',True)]:
                with self.assertRaises(ValueError): a.create(key,qty)
        finally: a.close()
