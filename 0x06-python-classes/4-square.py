#!/usr/bin/python3
""" the module """


class Square:
    """ the square class """
    def __init__(self, size=0):
        """ init function to initialize square
        Args: size(int): the size of square
        """
        self.__size = size

    @property
    def size(self):
        """
        size getter
        """
        return self.__size

    @size.setter
    def size(self, value):
        """
        size setter
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """
        the area
        """
        return self.__size * self.__size
