import tempfile, unittest
from pathlib import Path
from app import Worker
class Tests(unittest.TestCase):
    def test_redelivery_after_restart(self):
        with tempfile.TemporaryDirectory() as d:
            p=Path(d)/'queue'; sink=[]; w=Worker(p); w.enqueue('e1'); w.enqueue('e1')
            with self.assertRaises(RuntimeError): w.run(sink,crash=True)
            w.close(); w=Worker(p); w.run(sink); w.run(sink)
            self.assertEqual(['e1'],sink)
            self.assertEqual(1,w.db.execute('SELECT sent FROM events').fetchone()[0]); w.close()
