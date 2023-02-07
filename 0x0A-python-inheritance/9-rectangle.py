#!/usr/bin/python3

"""
Full rectangle implementation based on 7-base_geometry

"""
BaseGeometryV3 = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometryV3):
    """
    Class rectangle child of basegeom
    Full rectangle implementation

    """

    def __init__(self, width, height):
        super().__init__()
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """
        return area of the rectangle
        """
        return self.__width*self.__height

    def __str__(self):
        """
        return a string that is is used fo printing the module
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
