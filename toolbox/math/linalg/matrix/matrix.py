"""
matrix.py

Author: Chris Oliver
Date: 24/07/2024
"""
from __future__ import annotations

from numbers import Number

from typing import List, Tuple, Union

__collections__ = Union[List, Tuple]


class Matrix:
    """
    Matrix class

    Attributes:
        rows: List[List[Number]]
        shape: Tuple[int, int]

    Methods:
        __init__(matrix: List[List[Number]]) -> None
        __getitem__(index: Union[Tuple[int, int], int]) -> Union[Number, List[Number]]
        __add__(other: Matrix) -> Matrix
        __mul__(other: Union[Matrix, Number]) -> Matrix
        __rmul__(other: Number) -> Matrix
    """

    def __init__(self, matrix: __collections__[[Number]]):
        if not isinstance(matrix, (list, tuple)):
            raise ValueError(f"Matrix must be a list or tuple, not {type(matrix)}")
        if not all(isinstance(row, (list, tuple)) for row in matrix):
            raise ValueError(f"Matrix rows must be lists or tuples, not {type(matrix)}")
        if not all(all(isinstance(col, Number) for col in row) for row in matrix):
            raise ValueError(f"Matrix elements must be numbers, not {"".join([str(type(col)) if not isinstance(col, Number) else "" for row in matrix for col in row])}")

        if len(matrix) == 0:
            raise ValueError("Matrix must have at least one row")
        if len(set(len(row) for row in matrix)) != 1:
            raise ValueError(f"Matrix rows must have the same length, got {[len(row) for row in matrix]}")

        self.rows = [list(row) for row in matrix]
        self.shape = (len(self.rows), len(self.rows[0]))

    def __getitem__(self, index: Union[Tuple[int, int], int]) -> Union[Number, List[Number]]:
        if isinstance(index, tuple) and len(index) == 2:
            return self.rows[index[0]][index[1]]

        if isinstance(index, int):
            return self.rows[index]

        raise ValueError(f"Invalid index type, expected tuple[int, int] but got {type(index)}")

    def __add__(self, other: Matrix) -> Matrix:
        if not isinstance(other, Matrix):
            raise ValueError(f"Unsupported operand type(s) for +: {type(self)} and {type(other)}")

        if self.shape != other.shape:
            raise ValueError(f"Matrices must have the same shape, got {self.shape} and {other.shape}")

        return Matrix([[self.rows[i][j] + other.rows[i][j] for j in range(self.shape[1])]
                       for i in range(self.shape[0])])

    def __mul__(self, other: Union[Matrix, Number]):
        if isinstance(other, Matrix):
            if self.shape[1] != other.shape[0]:
                raise ValueError(f"Matrix multiplication not possible with shapes {self.shape} and {other.shape}")
            return Matrix([[sum(self.rows[i][k] * other.rows[k][j] for k in range(self.shape[1]))
                            for j in range(other.shape[1])]
                           for i in range(self.shape[0])])

        if isinstance(other, Number):
            return Matrix([[self.rows[i][j] * other for j in range(self.shape[1])]
                           for i in range(self.shape[0])])

        raise ValueError(f"Unsupported operand type(s) for *: {type(self)} and {type(other)}")

    def __rmul__(self, other: Number) -> Matrix:
        return self * other

    def __pow__(self, power, modulo=None):
        if power == -1:
            raise ValueError("Matrix inversion not implemented yet")
        raise NotImplementedError("Matrix power calculation not implemented yet")