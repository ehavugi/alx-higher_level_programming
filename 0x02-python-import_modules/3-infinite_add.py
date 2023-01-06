#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":
    n_args = len(argv) - 1
    total = 0
    for i in range(1, len(argv)):
        total += int(argv[i])
    print(total)
