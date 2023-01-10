#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for j in range(len(row)):
            if j != len(row) - 1:
                ender = " " 
            else:
                ender = ""
            print("{:d}".format(row[j]), end= ender)
        print("")
