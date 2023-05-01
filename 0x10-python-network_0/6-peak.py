#!/usr/bin/python3
"""Model for finding peaks
Author: Emmanuel HAVUGIMANA
Date : 2023
For : ALX
"""


def find_peak(list_of_integers):
    """input: list of integers as input
        returns the peak
    """
    n = len(list_of_integers)
    if n <= 3:
        if n == 1:
            return list_of_integers[0]
        if n <= 1:
            return
        return max(list_of_integers)
    else:
        a = list_of_integers[0]
        b = list_of_integers[1]
        c = list_of_integers[2]
        if b > a and b > c:
            return b
        a = list_of_integers[-3]
        b = list_of_integers[-2]
        c = list_of_integers[-1]
        if b > a and b > c:
            return b
        return find_peak(list_of_integers[1:-1])
