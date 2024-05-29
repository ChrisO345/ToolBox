"""
timeit.py

Author: Chris Oliver
Date: 29/05/2024
"""


from time import perf_counter as pc
from typing import Callable


def timeit(func: Callable):
    """
    Decorator to measure the execution time of a function and print the result.

    This decorator takes a callable object (`func`) and wraps it to measure its
    execution time. When the decorated function is called, the decorator records
    the start and end times, calculates the difference, and prints a message
    indicating the function name and execution time in seconds.

    The decorator itself returns the wrapped function.

    Parameters
    ----------
    func : callable
           The callable object whose execution time to measure.

    Returns
    -------
    The wrapped function with added time measurement functionality.
    """
    def wrapper(*args, **kwargs):
        """
        Parameters
        ----------
        args
        kwargs
        """
        start = pc()
        func(*args, **kwargs)
        end = pc()
        time_taken = end - start
        print(f"{func.__name__} took {end - start:_format} seconds.")

    return wrapper


if __name__ == '__main__':
    pass
