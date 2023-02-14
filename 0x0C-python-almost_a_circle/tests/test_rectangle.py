
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
