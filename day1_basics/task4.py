from contextlib import contextmanager
import time

@contextmanager
def timer(name: str):
    before = time.perf_counter()
    yield
    after = time.perf_counter() - before
    print(f'{name} overall took {after:.2f} seconds')


with timer('download'):
    time.sleep(1.5)
