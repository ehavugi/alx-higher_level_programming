#!/usr/bin/python3

"""
    Rectangle class V0.0
    inherents Base
"""

from models.base import Base


class Rectangle(Base):
    """
        Rectangle class inherests Base
        version 0: init
        version 1: added atributes
        version 2: added area
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
            Initialization method
            Return: an instance
        """
        super().__init__(id)
        self.x = x
        self.y = y
        self.height = height
        self.width = width

    def update(self, *args, **kwargs):
        """
            update rectangle values
                1st argument : id attribute
                2nd agrument : width attribute
                3rd argument : height attribute
                4th argument : x
                5th argument : y
        """
        if len(args) == 0:
            if kwargs is not None:
                for key in kwargs.keys():
                    if key == "y":
                        self.y = kwargs['y']
                    if key == "x":
                        self.x = kwargs['x']
                    if key == "width":
                        self.width = kwargs['width']
                    if key == "height":
                        self.height = kwargs['height']
                    if key == "id":
                        self.id = kwargs['id']
        n = len(args)
        if n >= 1:
            self.id = args[0]
        if n >= 2:
            self.width = args[1]
        if n >= 3:
            self.height = args[2]
        if n >= 4:
            self.x = args[3]
        if n >= 5:
            self.y = args[4]

    def area(self):
        """
            compute the area of rectangle
            Return: Area
        """
        return self.__height*self.__width

    def display(self):
        """
            displays the rectangle
            Return: None
        """
        for i in range(self.y):
            print()
        if self.width * self.height == 0:
            print()
        else:
            for i in range(self.height):
                print(" "*self.x+"#"*self.width)

    def __str__(self):
        """
            return a printable string describing a rectangle
        """
        x = "[Rectangle] ({}) {}/{}".format(self.id, self.x, self.y)
        x = x + " - {}/{}".format(self.width, self.height)
        return (x)

    @property
    def width(self):
        """
        read width property
        """
        return self.__width

    @property
    def height(self):
        """
        getter for height
        """
        return self.__height

    @width.setter
    def width(self, width):
        """
            setter for height attribute
            Return: None
        """
        if isinstance(width, int):
            if (width > 0):
                self.__width = width
            else:
                raise ValueError("width must be > 0")
        else:
            raise TypeError("width must be an integer")

    @height.setter
    def height(self, height):
        """
            setter for height attribute
        """
        if isinstance(height, int):
            if (height > 0):
                self.__height = height
            else:
                raise ValueError("height must be > 0")
        else:
            raise TypeError("height must be an integer")

    @property
    def x(self):
        """
            getter for x attribute
        """
        return self.__x

    @x.setter
    def x(self, x):
        """
            setter forx attribute
        """
        if isinstance(x, int):
            if (x >= 0):
                self.__x = x
            else:
                raise ValueError("x must be >= 0")

        else:
            raise TypeError("X must be an integer")

    @property
    def y(self):
        """
            getter for y attrr
        """
        return self.__y

    @y.setter
    def y(self, y):
        """
            setter for y attribute
        """
        if isinstance(y, int):
            if (y >= 0):
                self.__y = y
            else:
                raise ValueError("y must be >= 0")
        else:
            raise TypeError("Y must be an integer")
