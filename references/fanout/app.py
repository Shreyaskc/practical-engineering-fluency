import asyncio
async def enrich(items, fetch, limit=3):
    if type(limit) is not int or limit < 1: raise ValueError('positive limit required')
    gate=asyncio.Semaphore(limit)
    async def one(item):
        async with gate: return await fetch(item)
    tasks=[asyncio.create_task(one(x)) for x in items]
    try: return await asyncio.gather(*tasks)
    finally:
        for task in tasks:
            if not task.done(): task.cancel()
        await asyncio.gather(*tasks,return_exceptions=True)
