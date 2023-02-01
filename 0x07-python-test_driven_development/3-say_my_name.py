#!/usr/bin/python3
"""
Say my Name module

"""


def say_my_name(first_name, last_name=""):
    """
    say_my_name takes a firstname, and an optional last name
    and print the name
    >>> say_my_name("John", "Smith")
    My name is John Smith
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
