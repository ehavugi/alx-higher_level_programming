#!/usr/bin/python3


"""
Square implementation v2
added size private attribute to square v0
"""


class Square:
    """
    improved Square implementation v2
    new features on top of v1
        1. default size set to 0
        2. type and value checking added to v1
    """
    def __init__(self, size=0):
        """
        Initialize the class by setting its attributes
        """
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
