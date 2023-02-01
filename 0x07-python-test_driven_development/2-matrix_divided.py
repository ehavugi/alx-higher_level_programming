#!/usr/bin/python3

"""
Matrix division module  v0
A matrix is  alist of list
divisor divide the matrix by a number
"""


def matrix_divided(matrix, div):
    """
    divide a matrix by a number div
    """
    str1 = "matrix must be a matrix (list of lists) of integers/floats"
    error1 = TypeError(str1)
    if type(matrix) != list:
        raise error1
    if len(matrix) == 0:
        raise error1
    if type(matrix[0]) != list:
        raise error1
    for column in matrix:
        if type(column) != list:
            raise error1
        for j in column:
            if type(j) in [int, float]:
                pass
            else:
                raise error1

    """ check if matrix has same number of elements in each now """
    x = len(matrix[0])
    for row in matrix:
        if len(row) != x:
            raise TypeError("Each row of the matrix must have the same size")

    """ check if dvi is a float or int"""
    if not (type(div) in [float, int]):
        raise TypeError("div must be a number")

    """ Check if div is not zero"""
    if div == 0:
        raise ZeroDivisionError("division by zero")

    new = []
    index = 0
    for row in matrix:
        rowi = []
        for column in row:
            rowi.append(round(column / div, 2))
        new.append(rowi)
        index += 1
    return new
