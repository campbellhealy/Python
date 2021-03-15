# my_logger.py
from functools import wraps


def my_logger(original_func):
    import logging

    logging.basicConfig(filename=f"{original_func.__name__}.log", level=logging.INFO)

    @wraps(original_func)
    def inner(*args, **kwargs):
        logging.info(f"Ran with args:{args},and kwargs {kwargs}")
        return original_func(*args, **kwargs)

    return inner
