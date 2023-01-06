#!/usr/bin/python3

from sys import argv

if __name__ == "__main__":
    n_args = len(argv) - 1
    if n_args == 0:
        print("0 arguments.")
        exit(0)
    if n_args == 1:
        print("1 argument:")
    else:
        print("{} arguments:".format(n_args))
    for i in range(1, len(argv)):
        print("{}: {}".format(i, argv[i]))
