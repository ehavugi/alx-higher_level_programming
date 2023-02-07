#!/usr/bin/python3

"""
MyInt implementation. The ALx rebel int
!= and == are inverted
"""


class MyInt(int):
    """
    the rebel int class
    """

    def __init__(self, value):
        """
        Initialize the int
        """
        self.__value = value

    def __eq__(self, other):
        """
        the inverted equal is neq
        """
        return self.__value != other

    def __ne__(self, other):
        """
        The inverted neq is eq
        """
        return self.__value == other
