import httpx
import time

URLS = [f"https://jsonplaceholder.typicode.com/posts/{i}" for i in range(1, 31)]
URLS.append("https://jsonplaceholder.typicode.com/posts/9999")

def fetch_sync() -> list[dict]:
    results = []
    with httpx.Client(timeout=30.0) as client:
        for url in URLS:
            try:
                r = client.get(url)
                r.raise_for_status()  # бросит ошибку если статус 4xx/5xx
                results.append(r.json())
            except httpx.TimeoutException:
                print(f"  timeout: {url}")
            except httpx.HTTPStatusError as e:
                print(f"  bad status {e.response.status_code}: {url}")
            except httpx.RequestError as e:
                print(f"  request failed: {url} ({e})")
    return results

start = time.perf_counter()
data = fetch_sync()
print(f"Sync: {time.perf_counter() - start:.2f}s, {len(data)} items")