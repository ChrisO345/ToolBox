"""
polynomial_regression.py

Author: Chris Oliver
Date: 29/05/2024
"""

from typing import Iterable
import numpy as np
from .vandermonde import vandermonde


def quadratic_regression(ti: Iterable, yi: Iterable, dims: int = 3) -> np.ndarray:
    """
    Performs quadratic regression to find the quadratic that best
        fits the supplied data.

    Parameters
    ----------
    ti : np.ndarray
         Measurement points, t_i, of the sampled data.
    yi : np.ndarray
         Measurement points, y_i, of the sampled data.
    dims : int
           Optional, The order of the polynomial to fit. Defaults to 3

    Returns
    -------
    a : np.ndarray
        The coefficients of the regression function that best fits the data

    Raises
    ------
    TypeError
        If dims is not an integer.
    ValueError
        If dims is less than 1.
    """

    if not isinstance(ti, np.ndarray):
        ti = np.array(ti)

    if not isinstance(yi, np.ndarray):
        yi = np.array(yi)

    if not isinstance(dims, int):
        types = str(type(dims)).split()[1][:-1:]
        raise TypeError(f"'{types}' object cannot be interpreted as an integer")

    if dims < 1:
        raise ValueError("math domain error")

    A, b = vandermonde(ti, yi, dims)
    # TODO: use a custom linear algorithm solver to avoid numpy dependency
    a = np.linalg.solve(A, b)
    return a
