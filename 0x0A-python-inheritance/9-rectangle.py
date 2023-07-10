#!/usr/bin/python3
""" Full Rectangle """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ Rectangle that inherits BaseGeometry """
    def __init__(self, width, height):
        """
        initialize the function
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """ the area of the rectangle """
        return self.__width * self.__height

    def __str__(self):
        """ return a string """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
