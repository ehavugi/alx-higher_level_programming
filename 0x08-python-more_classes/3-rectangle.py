#!/usr/bin/python3

"""
+ v1: empty rectangle
+ implements  class Rectangle v2

"""


class Rectangle:
    """
    An empty classs

    """
    def __init__(self, width=0, height=0):
        """
        class initialization
        """
        pass
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """
        get value of width
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        set width value
        """
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value < 0:
            return ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        return height of the rectangle
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        sets the value of height to new value
        """
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
        return area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        return perimeter of the rectangle
        """
        if (self.__width * self.__height) == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """
        return strrign to be printed
        """
        out = ""
        if (self.__width * self.__height == 0):
            return out
        for i in range(self.__height):
            out += "#" * self.__width
            if i < self.height-1:
                out += "\n"

        return out
