#!/usr/bin/python3

"""
Module on check if an object is a subclass of a class

"""


def inherits_from(obj, a_class):
    """
    check if an obj is instance of a class that inherited
    from  the specified class
    """
    if obj.__class__ == a_class:
        return False
    return (issubclass(type(obj), a_class))
