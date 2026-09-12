import time


def chunk_list(items, size):
    """Splits a list into smaller sublists of specified size.
    
    Args:
        items (list): The list to be divided.
        size (int): The size of each chunk.
    
    Returns:
        list: A list of sublists, each of size specified or less.
    """
    return [items[i:i + size] for i in range(0, len(items), size)]


def slugify(text):
    """Converts a string into a URL-friendly slug.
    
    Args:
        text (str): The input string to be slugified.
    
    Returns:
        str: A hyphen-separated lowercase representation of the input text.
    """
    return "-".join(text.lower().split())


def retry(fn, attempts=3, delay=1):
    """Retries a given function a specified number of times on failure.
    
    Args:
        fn (function): The function to invoke and retry.
        attempts (int, optional): Number of retry attempts. Defaults to 3.
        delay (int, optional): Delay between retries in seconds. Defaults to 1.
    
    Returns:
        object: The return value of the function if it succeeds.
    
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
    """Simple in-memory cache with a time-to-live (TTL) mechanism.
    
    Attributes:
        _ttl (int): Time-to-live in seconds for cached items.
        _store (dict): Internal storage for cached key-value pairs.
    
    Methods:
        get(key): Retrieve the cached value for the given key if it exists and is not expired.
        set(key, value): Store a new key-value pair in the cache.
    """
    def __init__(self, ttl_s=60):
    """Initializes a new Cache instance with a specified TTL.
    
    Args:
        ttl_s (int, optional): The time-to-live in seconds. Defaults to 60.
    """
        self._ttl = ttl_s
        self._store = {}

    def get(self, key):
    """Retrieves a value from the cache by key.
    
    Args:
        key (object): The key to search for in the cache.
    
    Returns:
        object: The cached value if it exists, otherwise None.
    """
        return self._store.get(key)

    def set(self, key, value):
    """Stores a value in the cache with the specified key.
    
    Args:
        key (object): The key to associate with the value.
        value (object): The value to store in the cache.
    """
        self._store[key] = value
