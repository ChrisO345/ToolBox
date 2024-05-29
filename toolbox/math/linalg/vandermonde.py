"""
vandermonde.py

Author: Chris Oliver
Date: 29/05/2024
"""

from typing import Iterable
import numpy as np


def vandermonde(ti: Iterable, yi: Iterable, dims: int = 3) -> (np.ndarray, np.ndarray):
    """
    Creates a nxn Vandermonde Matrix, and a nx1 column vector for use in
        quadratic regression

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
    A : np.ndarray
        Vandermonde matrix constructed from the measurement points.
    b : np.ndarray
        Column vector constructed from the measurement points and measurement values.

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

    A = np.zeros([dims, dims])
    b = np.zeros([dims, 1])

    sums = []

    for i in range(2 * dims - 1):
        sums.append(sum(t ** i for t in ti))

    for i in range(len(A)):
        for j in range(len(A)):
            A[i, j] = sums[i + j]

    for i in range(dims):
        b[i] = (sum(t ** i * y for (t, y) in zip(ti, yi)))

    return A, b
