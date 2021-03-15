# example.py
from functools import wraps


def my_logger(original_func):
    import logging

    logging.basicConfig(filename=f"{original_func.__name__}.log", level=logging.INFO)

    @wraps(original_func)
    def inner(*args, **kwargs):
        logging.info(f"Ran with args:{args},and kwargs {kwargs}")
        return original_func(*args, **kwargs)

    return inner


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


import time


@my_logger
@my_timer
def display_func(name, age):
    time.sleep(1)
    print(f"display_func ran with arguments {name} and {age}")


display_func("Joe", 44)
