#!/usr/bin/python3
""" rectangle test cases """


class RectangleTestCase(unittest.TestCase):
    def test_constructor(self):
        r = Rectangle(5, 10)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 0)
        self.assertEqual(r.y, 0)
        self.assertIsNone(r.id)

        r = Rectangle(5, 10, 2, 3, 12)
        self.assertEqual(r.width, 5)
        self.assertEqual(r.height, 10)
        self.assertEqual(r.x, 2)
        self.assertEqual(r.y, 3)
        self.assertEqual(r.id, 12)

    def test_width(self):
        r = Rectangle(5, 10)
        r.width = 8
        self.assertEqual(r.width, 8)

        with self.assertRaises(TypeError):
            r.width = "abc"
        with self.assertRaises(ValueError):
            r.width = -5

    def test_height(self):
        r = Rectangle(5, 10)
        r.height = 12
        self.assertEqual(r.height, 12)

        with self.assertRaises(TypeError):
            r.height = "abc"
        with self.assertRaises(ValueError):
            r.height = -10

    def test_x(self):
        r = Rectangle(5, 10)
        r.x = 3
        self.assertEqual(r.x, 3)

        with self.assertRaises(TypeError):
            r.x = "abc"

    def test_y(self):
        r = Rectangle(5, 10)
        r.y = 4
        self.assertEqual(r.y, 4)

        with self.assertRaises(TypeError):
            r.y = "abc"
