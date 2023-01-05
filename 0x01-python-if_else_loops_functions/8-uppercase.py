#!/usr/bin/env python3

def uppercase(str):
    size = len(str)
    ender = ""
    for i in range(size):
        c = str[i]
        if i == size - 1:
            ender = "\n"
        if ord(c) <= 122 and ord(c) >= 97:
            print("{}".format(chr(ord(c)-32)), end=ender)
        else:
            print("{}".format(c), end=ender)
