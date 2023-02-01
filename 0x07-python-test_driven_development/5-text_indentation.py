#!/usr/bin/python3


"""
text indentation module
include a text_indentation function
"""


def text_indentation(text):
    """
    text indentation function add two new lines after each ., ? or :
    >>> text_indentation("?34")
    ?

    34
    """
    new = text.replace(".", ".\n\n")
    new = new.replace("?", "?\n\n").replace(":", ":\n\n")
    print(new, end="")
