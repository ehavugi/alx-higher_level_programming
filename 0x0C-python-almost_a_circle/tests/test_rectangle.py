#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle


class RectangleTests(unittest.TestCase):
    """
    Rectangle test class
    """
    def test1(self):
        r1 = Rectangle(10,2)
        assert(r1.id == 3)

    def test2(self):
        r2 = Rectangle(2,10)
        assert(r2.id == 4)

    def test3(self):
        r3 = Rectangle(10, 2, 0, 0, 12)
        assert(r3.id == 12)

    def testArea(self):
        r4 = Rectangle(10,2, 0, 0, 15)
        assert(r4.area() == 20)

    def testUpdate1(self):
        r1 = Rectangle(10, 10, 10, 10)
        assert(r1.area() == 100)
        
        r1.update(89)
        assert(r1.id == 89)
        
        r1.update(89, 2)
        assert(r1.area()  == 20)

        r1.update(89, 2, 3)
        assert(r1.area() == 6)
        r1.update(89, 2, 3, 4)
        assert(r1.x == 4)
        r1.update(89, 2, 3, 4, 5)
        assert(r1.y == 5)
    def testUpdate2(self):
        r1 = Rectangle(10, 10, 10, 10)
        assert(r1.area() == 100)

        r1.update(height=1)
        assert(r1.area() == 10)

        r1.update(width=1, x=2)
        assert(r1.x == 2)

        r1.update(x=2, height=2, y=3, width=4)
        assert(r1.area() == 8)
