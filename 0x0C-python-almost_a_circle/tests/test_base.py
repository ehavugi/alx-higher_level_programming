#!/usr/bin/python3
import unittest
from models.base import Base

class BaseTests(unittest.TestCase):
    def test1(self):
        b1 = Base()
        assert(b1.id == 1)
    def test2(self):
        b2 = Base()
        assert(b2.id == 2)
