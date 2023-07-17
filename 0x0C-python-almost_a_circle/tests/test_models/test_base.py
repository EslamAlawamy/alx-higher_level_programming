#!/usr/bin/python3
""" unuttest """
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
    """ test base class """
    def test_id(self):
        """ id test func """
        base0 = Base()
        self.assertEqual(base0.id, 1)
        base1 = Base()
        self.assertEqual(base1.id, 2)
        base2 = Base(69)
        self.assertEqual(base2.id, 69)
        base3 = Base(-69)
        self.assertEqual(base3.id, -69)
        base4 = Base(0)
        self.assertEqual(base4.id, 0)
