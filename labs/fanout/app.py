import asyncio
async def enrich(items, fetch, limit=3):
    return await asyncio.gather(*(fetch(x) for x in items))
