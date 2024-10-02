import time
from functools import wraps

def retry(exceptions, tries=3, delay=2):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            attempt = 0
            while attempt < tries:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    print(f"Error: {e}, retrying in {delay}s...")
                    attempt += 1
                    time.sleep(delay)
            raise Exception(f"Failed after {tries} attempts")
        return wrapper
    return decorator
