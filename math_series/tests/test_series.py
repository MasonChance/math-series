from math_series import __version__

from math_series import series 


def test_version():
    assert __version__ == '0.1.0'

def test_fib_num():
    actual = series.fib_num(5)
    expected = 3
    assert actual == expected 


def test_lucas_num():
    actual = series.lucas_num(5)
    expected = 7
    assert actual == expected

def test_sum_series_default():

    actual = series.sum_series(5)
    expected = 3

    assert actual == expected

def test_sum_series_opt_lucas():
    actual = series.sum_series(5, 2, 1)
    expected = 7
    assert actual == expected


def test_sum_series_opt_any():
    actual = series.sum_series(8, 2, 6)
    expected = 94
    assert actual == expected

