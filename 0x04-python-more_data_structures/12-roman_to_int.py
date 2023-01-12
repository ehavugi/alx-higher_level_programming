#!/usr/bin/python3

def roman_to_int(roman_string):
    if not (isinstance(roman_string, str)):
        return 0
    decode = {
            "M": 1000,
            "D": 500,
            "C": 100,
            "L": 50,
            "X": 10,
            "V": 5,
            "I": 1
            }
    tot = 0
    prev = 5000
    for i in roman_string:
        curr = decode[i]
        if curr > prev:
            tot += curr - 2 * prev
        else:
            tot += curr
        prev = curr
    return tot
