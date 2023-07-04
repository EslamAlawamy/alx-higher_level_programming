#!/usr/bin/python3
""" Real definition of a rectangle """


class Rectangle:
    """ Rectangle class """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """ width getter of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """ width setter pf rectangle """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ getter the height of rectangle """
        return self.__height

    @height.setter
    def height(self, value):
        """ setter of the height of rectangle """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
