"""
isum.py

Author: Chris Oliver
Date: 29/05/2024
"""

from typing import Union, Iterable
from numbers import Number
from six import string_types


def isum(*numbers: Union[Iterable, Number]) -> Number:
    """
    Calculates the sum of numeric elements within nested iterables.

    This function takes any number of arguments, which can be either numeric values
    or iterables containing numeric values (including nested iterables). It
    recursively iterates through the arguments, summing all numeric elements
    encountered.


    Parameters
    ----------
    *numbers : Union[Iterable, Number]
              An iterable containing numeric values or nested iterables of numeric values.

    Returns
    -------
    The sum of all numeric elements within the provided iterables.

    Raises
    ------
    TypeError
        If any element in the input is not a numeric type (int, float, complex).
    """
    if len(numbers) == 1:
        numbers = numbers[0]
    total: Number = 0
    for item in numbers:
        if isinstance(item, Number):
            total += item
            continue
        if isinstance(item, Iterable) and not isinstance(item, string_types):
            total += isum(item)
            continue
        types = str(type(item)).split()[1][:-1:], str(type(total)).split()[1][:-1:]
        types_error = f"unsupported operand type(s) for +: {types[0]} and {types[1]}"
        raise TypeError(types_error)
    return total
