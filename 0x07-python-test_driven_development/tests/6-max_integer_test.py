#!/usr/bin/python3

"""
Unittest for max_integer([..])
tests cover empty list and a sample list
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """
    Unit test class
    manages tests for max_integer
    """

    def test_1(self):
        self.assertEqual(max_integer([1, 2, 3, 4]),4)

    def test_2(self):
        self.assertEqual(max_integer([9,3,-3,4]),9)
    
    def test_all_negative(self):
        self.assertEqual(max_integer([-1,-3,-5]), -1)

    def test_1value(self):
        self.assertEqual(max_integer([0]), 0)

    def test_middle(self):
        self.assertEqual(max_integer([1,2,9,0,2]),9)
