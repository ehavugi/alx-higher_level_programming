#!/usr/bin/python3

"""
Module for adding new attribute to any class
without using try and except
"""


def add_attribute(obj, name, value):
    """
    add attribute with name whose value value to obj
    """

    obj_str = str(obj.__class__).split("'")[1]
    if obj_str in __builtins__:
        raise TypeError("can't add new attribute")
    else:
        setattr(obj, name, value)
