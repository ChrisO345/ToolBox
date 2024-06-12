"""
windows.py

Author: Chris Oliver
Date: 13/06/2024
"""

from typing import Collection, Generator, Iterable


def sliding_window(iterable: Collection, size: int, step: int = 1) -> Generator[Iterable, None, None]:
    """
    Returns a generator that yields a sliding window of the collection.

    Parameters
    ----------
    iterable : Collection
               The Collection from which the sliding windows will be generated.
    size : int
           The size of each window.
    step : int
           Optional, the step size between each window. Defaults to 1


    Yields
    -------
    Generator[Iterable, None, None]

    Raises
    ------
    ValueError
        If `iterable` is not a collection.
        If `size` is not an integer.
        If `step` is not an integer.
        If `size` is less than or equal to 0.
        If `step` is less than or equal to 0.

    """
    if not isinstance(iterable, Collection):
        raise ValueError("iterable needs to be of type Collection")

    if not isinstance(size, int):
        raise ValueError("size needs to be of type int")

    if not isinstance(step, int):
        raise ValueError("step needs to be of type int")

    if size <= 0:
        raise ValueError("size needs to be a positive integer")

    if step <= 0:
        raise ValueError("step needs to be a positive integer")

    length = len(iterable)

    if length < size:
        yield iterable
        return

    idx = 0
    while _next := idx + size <= length:
        yield iterable[idx:_next]
        idx += step


def rolling_window():
    """
        Raises
        ------
        NotImplementedError
        """
    raise NotImplementedError("rolling_window() has not yet been implemented")
