#!/usr/bin/python3
""" Square #2 """
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ class Square that inherits Rectangle """
    def __init__(self, size):
        """ initiaalize the func """
        self.__size = size
        self.integer_validator("size", size)
        super().__init__(size, size)

    def area(self):
        """ the area of the square """
        return self.__size * self.__size

    def __str__(self):
        """ return string """
        return "[Square] {}/{}".format(self.__size, self.__size)
