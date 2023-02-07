#!/usr/bin/python3

"""
Is kinda of a class module

"""


def is_kind_of_class(obj, a_class):
    """
    return true if obj is an instance or a_class or of
    class that is derived from a_class
    """
    return issubclass(type(obj), a_class)
