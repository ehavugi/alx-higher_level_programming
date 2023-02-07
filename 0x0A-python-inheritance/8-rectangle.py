#!/usr/bin/python3

"""
V3 of basegeom

"""
BaseGeometryV3 = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometryV3):
    """
    Class rectangle child ogf basegeom
    """

    def __init__(self, width, height):
        super().__init__()
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
