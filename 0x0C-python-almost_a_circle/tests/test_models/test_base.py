#!/usr/bin/python3
""" unuttest """
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
        """ test base class """
    def setUp(self):
        """ setUp """
        Base._Base__nb_objects = 0

    def test_base_id_assigned(self):
        """ test_base_id_assigned """
        b = Base(10)
        self.assertEqual(b.id, 10)

    def test_base_increment_id(self):
        """ test_base_increment_id """
        b1 = Base()
        b2 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
