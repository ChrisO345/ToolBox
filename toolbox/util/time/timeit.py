from time import perf_counter as pc
from typing import Callable


def timeit(func: Callable):
    """
    TODO: docstrings

    :param func:
    :return:
    """
    def wrapper(*args, **kwargs):
        start = pc()
        func(*args, **kwargs)
        end = pc()
        time_taken = end - start
        print(f"{func.__name__} took {end - start:_format} seconds.")

    return wrapper


if __name__ == '__main__':
    pass
