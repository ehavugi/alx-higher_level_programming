#!/usr/bin/python3

"""
V3 of basegeom

"""
BaseGeometryV2 = __import__('6-base_geometry').BaseGeometry


class Rectangle(BaseGeometryV2):
    """
    Class rectangle child ogf basegeom
    """
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
