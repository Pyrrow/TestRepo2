import time


def chunk_list(items, size):
"""Splits a list into smaller chunks of a specified size.

Args:
    items (list): The list to be split.
    size (int): The size of each chunk.

Returns:
    list: A list of chunked sublists.
"""
    return [items[i:i + size] for i in range(0, len(items), size)]


def slugify(text):
"""Converts a string into a URL-friendly slug.

Args:
    text (str): The input text to be slugified.

Returns:
    str: A hyphen-separated lowercase string suitable for URLs.
"""
    return "-".join(text.lower().split())


def retry(fn, attempts=3, delay=1):
"""Attempts to execute a function with retries on failure.

Args:
    fn (callable): The function to be executed and retried.
    attempts (int, optional): The maximum number of attempts. Defaults to 3.
    delay (int, optional): The delay in seconds between attempts. Defaults to 1.

Returns:
    Any: The result of the function on success.

Raises:
    Exception: The last exception raised if all attempts fail.
"""
    last_exc = None
    for _ in range(attempts):
        try:
            return fn()
        except Exception as exc:
            last_exc = exc
            time.sleep(delay)
    raise last_exc


class Cache:
"""A simple in-memory cache implementation with a time-to-live (TTL) mechanism.

Attributes:
    _ttl (int): The time-to-live in seconds for cached items.
    _store (dict): An internal dictionary used to store key-value pairs.
"""
    def __init__(self, ttl_s=60):
"""Initializes a new Cache instance.

Args:
    ttl_s (int, optional): The time-to-live in seconds for cached items. Defaults to 60.
"""
        self._ttl = ttl_s
        self._store = {}

    def get(self, key):
"""Retrieves the value associated with the specified key.

Args:
    key (Any): The key to look up in the cache.

Returns:
    Any or None: The cached value, or None if the key is not present.
"""
        return self._store.get(key)

    def set(self, key, value):
"""Stores a key-value pair in the cache.

Args:
    key (Any): The key to be stored.
    value (Any): The value associated with the key.
"""
        self._store[key] = value
