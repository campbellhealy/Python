# decorators.py

# def mydecorator(function):
#     def wrapped(*args, **kwargs):
#         # Do stuff before original fuction call
#         result = function(*args, **kwargs)
#         # Do soomething after the function call
#         return result

#     # return wrapper as a decorated function
#     return wrapped

# def func():
#     """lorem ipsom"""

# @mydecorator
# def func():
#     """my docstring"""
#     print("hello")

# func.__doc__

from functools import wraps


def mydecorator(function):
    @wraps(function)


    def func():
        """should be preserved"""
        print("Hello")


func.__doc__


