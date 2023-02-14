from models.base import Base

"""
Rectangle class

"""


class Rectangle(Base):
    """
    Rectangle class inherests Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__x = x
        self.__y = y
        self.__height = height
        self.__width  = width

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width_set(self, width):

        if isinstance(width, int):
            if (width > 0):
                self.__width = width
            else:
                raise("width must be > 0")
        else:
            raise TypeError("width must be an integer")

    @height.setter
    def height_set(self, height):
        if isinstance(height, int):
            if (height > 0):
                self.__height = height
            else:
                raise ValueError("height must be > 0")
        else:
            raise TypeError("height must be an integer")

    @property
    def x(self):
        return self.__x

    @x.setter
    def x_set(self, x):
        if isinstance(x, int):
            if (x >= 0):
                self.__x = x
            else:
                raise ValueError("x must be >= 0")

        else:
            raise TypeError("X must be an integer")

    @property
    def y(self):
        return self.__y

    @y.setter
    def y_set(self, y):
        if True:
            if (y >= 0):
                self.__y = y
            else:
                raise ValueError("y must be >= 0")
        else:
            raise TypeError("Y must be an integer")
