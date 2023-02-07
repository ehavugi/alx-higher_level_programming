#!/usr/bin/python3

"""
Write file module

"""


def write_file(filename="", text=""):
    """
    write text to given file name, renaming a file if already exist
    """
    with open(filename, "w", encoding="utf-8") as f:
        return (f.write(text))
