#!/usr/bin/python3

"""
V3 of basegeom

"""
BaseGeometryV2 = __import__('6-base_geometry').BaseGeometry


class BaseGeometry(BaseGeometryV2):
    """
    Class rectangle child ogf basegeom
    """

    def area(self):
        """
        placeholder for area
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validation function
        Raises corresponding errors when there are
        """
        if value.__class__ == int:
            if value <= 0:
                raise ValueError(name + " must be greater than 0")
            else:
                pass
        else:
            raise TypeError(name + " must be an integer")
