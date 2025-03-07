"""
test_matrix.py

Author: Chris Oliver
Date: 07/03/2025
"""
import pytest


def test_matrix_create():
    from toolbox.math.linalg.matrix import Matrix

    m = Matrix([[1, 2], [3, 4]])
    assert m.shape == (2, 2)
    assert m.rows[0] == [1, 2]
    assert m.rows[1][0] == 3
    assert m.rows[1][1] == 4

    m = Matrix([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    assert m.shape == (3, 3)
    assert m[0] == [1, 2, 3]
    assert all(a == b for a, b in zip(m[1], [4, 5, 6]))
    assert all(a == b for a, b in zip(m[2], [7, 8, 9]))

    with pytest.raises(ValueError) as e:
        m = Matrix([[1, 2], [3, 4, 5]])
    assert "Matrix rows must have the same length, got [2, 3]" in str(e.value)

    with pytest.raises(ValueError) as e:
        m = Matrix([[1, 2], [3, '4']])
    assert "Matrix elements must be numbers, not <class 'str'>" in str(e.value)

    with pytest.raises(ValueError) as e:
        m = Matrix([])
    assert "Matrix must have at least one row" in str(e.value)


def test_matrix_add():
    from toolbox.math.linalg.matrix import Matrix

    m1 = Matrix([[1, 2], [3, 4]])
    m2 = Matrix([[5, 6], [7, 8]])

    result = m1 + m2
    assert result.shape == (2, 2)
    assert result[0] == [6, 8]
    assert result[1] == [10, 12]

    m3 = Matrix([[1, 2], [3, 4], [5, 6]])
    with pytest.raises(ValueError) as e:
        result = m1 + m3
    assert "Matrices must have the same shape, got (2, 2) and (3, 2)" in str(e.value)


def test_matrix_multiply():
    from toolbox.math.linalg.matrix import Matrix

    m1 = Matrix([[1, 2], [3, 4]])
    m2 = Matrix([[5, 6], [7, 8]])

    result = m1 * m2
    assert result.shape == (2, 2)
    assert result[0] == [19, 22]
    assert result[1] == [43, 50]

    result = m1 * 2
    assert result.shape == (2, 2)
    assert result[0] == [2, 4]
    assert result[1] == [6, 8]

    result = 2 * m1
    assert result.shape == (2, 2)
    assert result[0] == [2, 4]
    assert result[1] == [6, 8]

    m3 = Matrix([[1, 2], [3, 4], [5, 6]])
    with pytest.raises(ValueError) as e:
        result = m1 * m3
    assert "Matrix multiplication not possible with shapes (2, 2) and (3, 2)" in str(e.value)


# noinspection PyStatementEffect, PyTypeChecker
def test_matrix_getitem():
    from toolbox.math.linalg.matrix import Matrix

    m = Matrix([[1, 2], [3, 4]])

    assert m[0, 0] == 1
    assert m[0, 1] == 2
    assert m[1, 0] == 3
    assert m[1, 1] == 4

    assert m[0] == [1, 2]
    assert m[1] == [3, 4]

    with pytest.raises(ValueError) as e:
        m[0, 0, 0]
    assert "Invalid index type, expected tuple[int, int] but got <class 'tuple'>" in str(e.value)

if __name__ == '__main__':
    pytest.main()
