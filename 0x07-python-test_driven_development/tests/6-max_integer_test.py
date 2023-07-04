#!/usr/bin/python3
""" Max integer - Unittest """


import unittest
max_integer = __import__('6-max_integer').max_integer



class TestMaxInteger(unittest.TestCase):
    """ test max intger class """
    
    def test_empty_list(self):
        """ check if it's none """
        self.assertIsNone(max_integer([]), "the result should be None")
