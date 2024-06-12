"""
windows.py

Author: Chris Oliver
Date: 13/06/2024
"""

from typing import Collection, Generator, Iterable


def sliding_window(arr: Collection, k: int, step: int = 1) -> Generator[Iterable, None, None]:
    """
    Returns a generator that yields a sliding window of the collection.

    Parameters
    ----------
    arr : Collection
          The Collection from which the sliding windows will be generated.
    k : int
        The size of each window.
    step : int
           Optional, the step size between each window. Defaults to 1

    Yields
    -------
    Generator[Iterable, None, None]

    Raises
    ------
    ValueError
        If `arr` is not a collection.
        If `k` is not an integer.
        If `step` is not an integer.
        If `k` is less than or equal to 0.
        If `step` is less than or equal to 0.

    """
    if not isinstance(arr, Collection):
        raise ValueError("arr needs to be of type collection")

    if not isinstance(k, int):
        raise ValueError("k needs to be of type int")

    if not isinstance(step, int):
        raise ValueError("step needs to be of type int")

    if k <= 0:
        raise ValueError("k needs to be a positive integer")

    if step <= 0:
        raise ValueError("step needs to be a positive integer")

    length = len(arr)

    if length < k:
        yield arr
        return

    idx = 0
    while (_next := idx + k) <= length:
        yield arr[idx:_next]
        idx += step


def rolling_window(arr: Collection, k: int) -> Generator[Iterable, None, None]:
    """
    Returns a generator that yields a rolling window of the collection.

    Parameters
    ----------
    arr : Collection
          The Collection from which the sliding windows will be generated.
    k : int
        The size of each window.

    Yields
    -------
    Generator[Iterable, None, None]

    Raises
    ------
    ValueError
        If `arr` is not a collection.
        If `k` is not an integer.
        If `k` is less than or equal to 0.

    """
    if not isinstance(arr, Collection):
        raise ValueError("arr needs to be of type collection")

    if not isinstance(k, int):
        raise ValueError("k needs to be of type int")

    if k <= 0:
        raise ValueError("k needs to be a positive integer")

    window = []

    for i in range(len(arr)):
        window.append(arr[i])

        if len(window) > k:
            window.pop(0)

        if len(window) == k:
            yield window[:]
