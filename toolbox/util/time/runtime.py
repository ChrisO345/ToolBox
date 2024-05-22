from typing import Callable
from time import perf_counter as pc


def runtime(func: Callable, *args, **kwargs) -> float:
    """
    TODO: docstrings
    :param func:
    :param args:
    :param kwargs:
    :return:
    """
    start = pc()
    func(*args, **kwargs)
    end = pc()
    return end - start
