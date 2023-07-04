#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer


class TestMaxInteger(unittest.TestCase):
    """ test max intger class """


    def test_empty_list(self):
        """ check if it's none """
        self.assertEqual(max_integer([]), None)

    def test_repeted_number(self):
        """ repeated number """
        self.assertEqual(max_integer([369, 369, 369, 369]), 369)

    def test_one_element(self):
        """ one element """
        self.assertEqual(max_intger([69,]), 69)
