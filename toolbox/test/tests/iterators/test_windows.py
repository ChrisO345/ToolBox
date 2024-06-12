"""
test_windows.py

Author: Chris Oliver
Date: 13/06/2024
"""


def test_sliding_window():
    from toolbox.iterators.windows import sliding_window

    arr = [1, 2, 3, 4, 5]
    k = 3

    expected = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
    result = list(sliding_window(arr, k))

    assert result == expected


def test_rolling_window():
    from toolbox.iterators.windows import rolling_window

    arr = [1, 2, 3, 4, 5]
    k = 3

    expected = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
    result = list(rolling_window(arr, k))

    assert result == expected


if __name__ == '__main__':
    import pytest
    pytest.main()
