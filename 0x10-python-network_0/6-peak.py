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
        return find_peak([list_of_integers[0],
                         find_peak(list_of_integers[1:-1]),
                         list_of_integers[-1]])
