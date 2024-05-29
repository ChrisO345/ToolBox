"""
runtime.py

Author: Chris Oliver
Date: 29/05/2024
"""


from typing import Callable
from time import perf_counter as pc


def runtime(func: Callable, *args, **kwargs) -> float:
    """
    Measures the execution time of a function.

    This function takes a callable object (`func`) and any arguments (`*args`, `**kwargs`)
    to be passed to that function. It returns the time elapsed in seconds between
    when `func` starts and finishes execution. Note that the measurement excludes
    the time taken by `runtime` itself.

    Parameters
    ----------
    func : callable
           The callable object whose execution time to measure.
    *args
           Positional arguments to be passed to `func`.
    **kwargs
           Keyword arguments to be passed to `func`.

    Returns
    -------
    The execution time of `func` in seconds (float).
    """
    start = pc()
    func(*args, **kwargs)
    end = pc()
    return end - start
