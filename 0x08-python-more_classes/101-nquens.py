#!/usr/bin/python3
"""
n nqueens moves
"""
import sys

value = sys.argv[0]
try:
    if (str(int(value)) == value):
        new = int(value)
except Exception as e:
    print("N must be a number")
    return 1
if (new < 4):
    print("N must be at least 4")
    return 1

placed = []
placement = []
for i in range(new):
    if len(placement) == 0:
        placement = [0, 1]
        placed.append(placement)
    else:
        if placement in placed:
            pass
return placed
