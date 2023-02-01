#!/usr/bin/python3

"""
add_integer module  v0.0
includes
    1.doctests

"""


def add_integer(a, b=98):
    """
    >>> add_integer(1,1)
    2
    >>> add_integer(-8)
    90
    """
    if not (type(a) in [int, float]):
        raise (TypeError("a must be an integer"))
    if not (type(b) in [int, float]):
        raise (TypeError("b must be an integer"))

    return int(int(a) + int(b))
