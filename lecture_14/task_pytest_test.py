import pytest


def func(a, b=0, c=0):
    """Решение квадратного уравнения"""
    d = b ** 2 - 4 * a * c
    if d < 0:
        return None
    elif d == 0:
        return -b / (2 * a)
    else:
        x1 = (-b + d ** 0.5) / (2 * a)
        x2 = (-b - d ** 0.5) / (2 * a)
        return x1, x2


def test_1():
    assert func(4) == 0


def test_2():
    assert func(4, -4) == (1, 0)


def test_3():
    assert func(4, -10, -50) == (5, -2.5)


def test_4():
    assert func(1, 1, 1) is None


if __name__ == '__main__':
    pytest.main(['-v'])
