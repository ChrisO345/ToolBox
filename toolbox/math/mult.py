"""
mult.py

Author: Chris Oliver
Date: 29/05/2024
"""


from typing import Union, Iterable
from numbers import Number
from six import string_types


def mult(*numbers: Union[Iterable, Number]) -> Number:
    """
    Calculates the product of numeric elements within nested iterables.

    Parameters
    ----------
    *numbers : Union[Iterable, Number]
               An iterable containing numeric values or nested iterables of numeric values.

    Returns
    -------
    The product of all numeric elements within the provided iterables.

    Raises
    ------
    TypeError
        If any element in the input is not a numeric type (int, float).
    """
    if len(numbers) == 1:
        numbers = numbers[0]
    total: Number = 1
    for item in numbers:
        if isinstance(item, Number):
            total *= item
            continue
        if isinstance(item, Iterable) and not isinstance(item, string_types):
            total *= mult(item)
            continue
        types = str(type(item)).split()[1][:-1:], str(type(total)).split()[1][:-1:]
        types_error = f"unsupported operand type(s) for *: {types[0]} and {types[1]}"
        raise TypeError(types_error)
    return total
