import asyncio, unittest
from app import enrich
class Tests(unittest.IsolatedAsyncioTestCase):
    async def test_limit_and_order(self):
        active=peak=0
        async def fetch(x):
            nonlocal active,peak
            active+=1; peak=max(peak,active)
            try: await asyncio.sleep(0); return x*2
            finally: active-=1
        self.assertEqual([0,2,4,6,8,10],await enrich(range(6),fetch,2))
        self.assertLessEqual(peak,2); self.assertEqual(active,0)
    async def test_cancel_drains(self):
        entered=asyncio.Event(); active=0
        async def fetch(x):
            nonlocal active
            active+=1; entered.set()
            try: await asyncio.Event().wait()
            finally: active-=1
        task=asyncio.create_task(enrich(range(5),fetch,2))
        await entered.wait(); task.cancel()
        with self.assertRaises(asyncio.CancelledError): await task
        self.assertEqual(active,0)
    async def test_invalid(self):
        with self.assertRaises(ValueError): await enrich([],None,0)
