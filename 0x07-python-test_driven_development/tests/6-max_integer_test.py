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
        self.assertEqual(max_intger([69]), 69)

    def test_positive_list(self):
        """ positive list """
        self.assertEqual(max_intger([50, 60, 90, 100]), 100)

    def test_negative_list(self):
        """ negative list"""
        self.assertEqual(max_intger([-50, -100, -500, -25]), -25)

    def test_mixed_numbers(self):
        """ mixed numbers """
        self.assertEqual(max_intger([50, 60, -50, -15]), 60)

    def test_zero(self):
        """ zero """
        self.assertEqual(max_intger([0, 0, 0, 0]), 0)

    def test_float_number(self):
        """ float num """
        self.assertEqual(max_intger([1.5, 15.2, 20.3, 60.9]), 60.9)

    def test_int_with_float(self):
        """ int with float """
        self.assertEqual(max_intger([15, 70.5, 50, 18.8]), 70.5)

