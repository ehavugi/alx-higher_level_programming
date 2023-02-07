#!/usr/bin/python3
"""
Square module based on rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Square class
    """

    def __init__(self, size):
        """
        class initialized by validating size of square
        """
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
