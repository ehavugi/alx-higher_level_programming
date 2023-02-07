#!/usr/bin/python3
"""
Append to a text file
"""


def append_write(filename="", text=""):
    """
    add content to the file if exist.
    else create new file and write the content to it
    """
    with open(filename, 'a', encoding="utf-8") as f:
        return (f.write(text))
