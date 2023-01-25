#!/usr/bin/python3


"""
Square implementation v3
added area method to square v2
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
