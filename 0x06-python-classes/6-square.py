#!/usr/bin/python3


"""
Square implementation v5
added set method to set size to square v3
added my_print to v4
"""


class Square:
    """
    improved Square implementation v3
    new features on top of v1
        1. default size set to 0
        2. type and value checking added to v1
    Features on top of v2
        + get value of area of square
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize the class by setting its attributes
        """
        self.__size = size
        if type(size) != int:
            raise TypeError("size must be an integer")
        if (size < 0):
            raise ValueError("size must be >= 0")
        self.position_check(position)
        self.__position = position

    def position_check(self, position):
        """
        checks if position is compliant
        """
        if (type(position) == tuple):
            if len(position) == 2:
                a = position[0]
                b = position[1]
                if type(a) == type(b) == int and a >= 0 and b >= 0:
                    return
                
        raise TypeError("position must be a tuple of 2 positive integers")

    def area(self):
        """
        Returns the area of current square
        """
        return (self.__size)**2

    @property
    def size(self):
        """
        getter for size
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        Set value of size to value
        """
        if type(value) != int:
            raise TypeError("size must be an integer")
        if (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """
        returns position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        sets postion to new value
        """
        self.position_check(value)
        self.__position = value

    def my_print(self):
        """
        prints square made of #
        """
        size = self.__size
        position = self.__position
        if (size == 0):
            print()
        else:
            for p in range(position[1]):
                print()
            for i in range(size):
                for x in range(position[0]):
                    print(" ", end="")
                for j in range(size):
                    print("#", end='')
                print()
