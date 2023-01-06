#!/usr/bin/python3

def uppercase(str):
    size = len(str)
    ender = ""
    for i in range(size):
        c = str[i]
        if i == size - 1 or size == 0:
            ender = "\n"
        if ord(c) <= 122 and ord(c) >= 97:
            c = chr(ord(c)-32)
        print("{}".format(c), end="")
    print("")
