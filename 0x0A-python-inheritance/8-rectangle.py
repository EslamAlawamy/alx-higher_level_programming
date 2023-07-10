#!/usr/bin/python3
""" Rectangle """


class BaseGeometry:
    """ BaseGeometry class """
    def area(self):
        """
        raises an Exception with the
        message area() is not implemented
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        validates value
        """
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """ Rectangle that inherits BaseGeometry """
    def __init__(self, width, height):
        """
        initialize the function
        """
        self.__width = width
        self.integer_validator("width", width)
        self.__height = height
        self.integer_validator("height", height)
