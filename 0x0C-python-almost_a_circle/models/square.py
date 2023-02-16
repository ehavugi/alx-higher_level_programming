#!/usr/bin/python3

"""
    Square module --> Square class
        inherents Rectangle class
"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """
        Square class

    """

    def __init__(self, size, x=0, y=0, id=None):
        """
            initialize a rectangle by setting width = height = size.

        """
        super().__init__(size, size, x, y, id)
        self.size = size

    @property
    def size(self):
        """
            return size of square
        """
        return self.size

    @size.setter
    def size(self, size):
        """
            set width and height values
        """
        self.width = size
        self.height = size

    def __str__(self):
        """
            return [Square] (<id>) <x>/<y> - <size>
        """
        x = "[Square] ({}) ".format(self.id)
        x = x + "{}/{} {}".format(self.x, self.y, self.height)
        return x
