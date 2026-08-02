import time


def chunk_list(items, size):
    return [items[i:i + size] for i in range(0, len(items), size)]


def slugify(text):
    return "-".join(text.lower().split())


def retry(fn, attempts=3, delay=1):
    last_exc = None
    for _ in range(attempts):
        try:
            return fn()
        except Exception as exc:
            last_exc = exc
            time.sleep(delay)
    raise last_exc


class Cache:
    def __init__(self, ttl_s=60):
        self._ttl = ttl_s
        self._store = {}

    def get(self, key):
        return self._store.get(key)

    def set(self, key, value):
        self._store[key] = value
