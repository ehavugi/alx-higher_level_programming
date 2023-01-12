#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new = []
    for i in matrix:
        temp = []
        for j in i:
            temp.append(j ** 2)
        new.append(temp)
    return new
