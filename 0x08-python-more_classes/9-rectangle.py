#!/usr/bin/python3

"""
+ v1: empty rectangle
+ implements  class Rectangle v2

"""


class Rectangle:
    """
    An empty classs

    """
    number_of_instances = 0
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """
        class initialization
        """
        pass
        self.__width = width
        self.__height = height
        self.add_to_class()

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
            out += str(self.print_symbol) * self.__width
            if i < self.height-1:
                out += "\n"

        return out

    def __repr__(self):
        """
        return a string representation of instance that
        can be used to create the instance
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    @classmethod
    def __del__(cls):
        """
        execute on deletion of instance
        """
        print("Bye rectangle...")
        cls.number_of_instances -= 1

    @classmethod
    def add_to_class(cls):
        """
        add new instances
        """
        cls.number_of_instances += 1

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        returns biggest rectangle of rect1 and rect2
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Returns a Rectangle with height=width=size
        """
        return cls(size, size)
