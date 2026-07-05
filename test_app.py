"""Tiny test suite for ci-medic demos. One test fails on purpose."""


def add(a, b):
    return a + b


def divide(a, b):
    return a / b


def test_add():
    assert add(2, 3) == 5


def test_divide():
    assert divide(10, 2) == 5


def test_divide_by_zero_handling():
    # Intentional bug: this will raise ZeroDivisionError
    assert divide(10, 0) == 0