#!/usr/bin/python3


"""
Square implementation v4
added set method to set size to square v3
"""


class Square:
    """
    improved Square implementation v3
    new features on top of v1
        1. default size set to 0
        2. type and value checking added to v1
    Features on top of v2
        + get value of area of square
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

    def area(self):
        """
        Returns the area of current square
        """
        return (self.__size)**2

    @property
    def size(self):
        """
        getter for size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set value of size to value
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value
