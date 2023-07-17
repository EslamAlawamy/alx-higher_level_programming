#!/usr/bin/python3
""" rectangle test cases """
import unittest
from models.rectangle import Rectangle


class RectangleTestCase(unittest.TestCase):
    """ rectangle testcases """
    def test_constructor(self):
        """ test case """
        r = Rectangle(5, 10)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)
        self.assertIsNotNone(r.id)

        r = Rectangle(5, 10, 2, 3, 12)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 3)
        self.assertEqual(r.id, 12)

    def test_width_validation(self):
        """ test case """
        r = Rectangle(5, 10)
        r.width = 15
        self.assertEqual(r.width, 15)

        with self.assertRaises(TypeError):
            r.width = "invalid"
        with self.assertRaises(ValueError):
            r.width = -5

    def test_height_validation(self):
        """ test case """
        r = Rectangle(5, 10)
        r.height = 20
        self.assertEqual(r.height, 20)

        with self.assertRaises(TypeError):
            r.height = "invalid"
        with self.assertRaises(ValueError):
            r.height = -10

    def test_x_validation(self):
        """ test case """
        r = Rectangle(5, 10)
        r.x = 3
        self.assertEqual(r.x, 3)

        with self.assertRaises(TypeError):
            r.x = "invalid"
        with self.assertRaises(ValueError):
            r.x = -2

    def test_y_validation(self):
        """ test case """
        r = Rectangle(5, 10)
        r.y = 4
        self.assertEqual(r.y, 4)

        with self.assertRaises(TypeError):
            r.y = "invalid"
        with self.assertRaises(ValueError):
            r.y = -3

    def test_area(self):
        """ test case """
        r = Rectangle(5, 10)
        self.assertEqual(r.area(), 50)

        r.width = 15
        self.assertEqual(r.area(), 150)

    def test_display(self):
        """ test case """
        r = Rectangle(4, 6)
        expected_output = "####\n" * 6
        with unittest.mock.patch("sys.stdout", new=unittest.mock.StringIO()) as output:
            r.display()
            self.assertEqual(output.getvalue().strip(), expected_output.strip())

    def test_to_dictionary(self):
        """ test case """
        r = Rectangle(5, 10, 2, 3, 12)
        expected_dict = {
            "id": 12,
            "width": 5,
            "height": 10,
            "x": 2,
            "y": 3
        }
        self.assertDictEqual(r.to_dictionary(), expected_dict)

    def test_update_no_kwargs(self):
        """ test case """
        r = Rectangle(5, 10)
        r.update(20, 15, 2, 3)
        self.assertEqual(r.id, 20)
        self.assertEqual(r.width, 15)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 0)

    def test_update_with_kwargs(self):
        """ test case """
        r = Rectangle(5, 10)
        r.update(id=20, width=15, height=2, x=3, y=4)
        self.assertEqual(r.id, 20)
        self.assertEqual(r.width, 15)
        self.assertEqual(r.height, 2)
        self.assertEqual(r.x, 3)
        self.assertEqual(r.y, 4)
