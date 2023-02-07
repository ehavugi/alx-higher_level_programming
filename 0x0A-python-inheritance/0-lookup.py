#!/usr/bin/python3

"""
lookup module v0

"""


def lookup(object):
    """
    takes object and returns list of attributes and methods.
    >>> lookup(object)[:3] == ['__class__', '__delattr__', '__dir__']
    True
    """
    return dir(object)
