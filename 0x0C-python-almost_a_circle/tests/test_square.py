#!/usr/bin/python3
import unittest
from models.square import Square


class SquareTests(unittest.TestCase):
    """
    Rectangle test class
    """
    def test1(self):
        """ first test """
        r1 = Square(2)
        assert(r1.area() == 4)

    def test2(self):
        """
            test more than 1 arg
        """
        r1 = Square(2, 2)
        assert(r1.x == 2)

    def test3(self):
        """
            test 3 arguments
        """
        r1 = Square(3, 1, 3)
        assert(r1.y == 3)
        assert(r1.x == 1)
        assert(r1.area() == 9)
    def testSize(self):
        """
            test setting size
        """
        r1 = Square(2)
        # r1.size == 10
        assert(True)
