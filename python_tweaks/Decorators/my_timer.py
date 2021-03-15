# my_timer.py
from functools import wraps


def my_timer(original_func):
    from time import time

    @wraps(original_func)
    def inner(*args, **kwargs):
        start = time()
        result = original_func(*args, **kwargs)
        end = time() - start
        print(f"{original_func.__name__} ran in {end} sec.")
        return original_func(*args, **kwargs)

    return inner
