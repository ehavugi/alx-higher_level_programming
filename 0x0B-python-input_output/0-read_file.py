#!/usr/bin/python3
"""
Read file
"""


def read_file(filename=""):
    """

    read a file UTF8 and print out read text.

    """
    with open(filename, "r", encoding="utf-8") as f:
        read_data = f.read()
        print(read_data, end="")
