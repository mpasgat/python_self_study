import asyncio
import httpx
import time

URLS = [f"https://jsonplaceholder.typicode.com/posts/{i}" for i in range(1, 31)]

async def fetch_one(client: httpx.AsyncClient, url: str) -> dict:
    r = await client.get(url)
    return r.json()

async def fetch_async() -> list[dict]:
    async with httpx.AsyncClient() as client:
        tasks = [fetch_one(client, url) for url in URLS]
        return await asyncio.gather(*tasks)

start = time.perf_counter()
data = asyncio.run(fetch_async())
print(f"Async: {time.perf_counter() - start:.2f}s, {len(data)} items")