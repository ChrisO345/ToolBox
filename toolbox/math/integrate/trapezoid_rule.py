"""
trapezoid_rule.py

Author: Chris Oliver
Date: 29/05/2024
"""

from typing import Iterable
import numpy as np


def trapezoid(tj: Iterable, yj: Iterable) -> float:
    """
    Uses the Newton-Cotes composite trapezoid rule to integrate
        between fixed space data points.

    Parameters
    ----------
    tj : np.ndarray
         Measurement points, t_j, of the integrand.
    yj : np.ndarray
         Measurement points, y_j, of the integrand.

    Returns
    -------
    integral : float
        Numerical Approximation of integral.

    Raises
    ------
    ValueError
        If tj and yj are not the same length.
        If tj and yj are less than 2 in length.
    """
    if not isinstance(tj, np.ndarray):
        tj = np.array(tj)

    if not isinstance(yj, np.ndarray):
        yj = np.array(yj)

    if tj.shape != yj.shape:
        raise ValueError("ti and yi must have the same first dimension")

    if len(tj) < 2:
        raise ValueError("tj and yj must be of length 2 or greater")

    step = tj[1] - tj[0]
    integral = float(.5 * step * (yj[0] + yj[-1] + 2 * sum(yj[1:-1])))
    return integral
