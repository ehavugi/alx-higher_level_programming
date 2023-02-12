from  models.base import Base

"""
Rectangle class

"""

class Rectangle(Base):

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id) 

    @property
    def __width(self):
        return self.__width
    @property
    def __height(self):
        return self.__height

    @__width.setter
    def width_set(self, width):
        if True:
            self.__width= width
        else:
            raise ValueError("width must be greater than 0")
    @__height.setter
    def height_set(self, height):
        if True:
            self.__height = height
        else:
            raise ValueError("Height must be than or equal to 0")

    @property
    def __x(self):
        return self.__x

    @__x.setter
    def x_set(self, x):
        if True:
            self.__x = x
        else:
            raise ValueError("X must be greater than or equal to 0")

    @property
    def __y(self):
        return self.__y

    @__y.setter
    def y_set(self, y):
        if True:
            self.__y = y
        else:
            raise ValueError("Y must be greater than or equal to 0")
