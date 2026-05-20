import asyncio
import httpx
import time

URLS = [f"https://jsonplaceholder.typicode.com/posts/{i}" for i in range(1, 31)]
URLS.append("https://jsonplaceholder.typicode.com/posts/9999")

async def fetch_one_limited(
    client: httpx.AsyncClient,
    url: str,
    sem: asyncio.Semaphore,
) -> dict | None:
    try:
        async with sem:
            r = await client.get(url)
            r.raise_for_status()
            return r.json()
    except httpx.TimeoutException:
        print(f"  timeout: {url}")
        return None
    except httpx.HTTPStatusError as e:
        print(f"  bad status {e.response.status_code}: {url}")
        return None
    except httpx.RequestError as e:
        print(f"  request failed: {url} ({e})")
        return None

async def fetch_async_limited(max_concurrent: int = 5) -> list[dict]:
    sem = asyncio.Semaphore(max_concurrent)
    async with httpx.AsyncClient() as client:
        tasks = [fetch_one_limited(client, url, sem) for url in URLS]
        result = await asyncio.gather(*tasks)
        return [r for r in result if r is not None]
    

start = time.perf_counter()
data = asyncio.run(fetch_async_limited())
print(f"Async: {time.perf_counter() - start:.2f}s, {len(data)} items")