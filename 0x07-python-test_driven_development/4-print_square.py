#!/usr/bin/python3

"""
function that prints square of side = size
symbol used is #
"""


def print_square(size):
    """
    print_square takes in size as side of square
    print a square made of '#' where size >= 0
    >>> print_square(3)
    ###
    ###
    ###

    """
    if type(size) == float and size < 0:
        raise TypeError("size must be an integer")
    if type(size) == float:
        size = int(size - 0.5)
    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    if size == 0:
        return
    for i in range(size):
        print("#" * size)
