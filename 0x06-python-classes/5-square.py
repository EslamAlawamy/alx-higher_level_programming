#!/usr/bin/python3
""" the main module """


class Square:
    """ square class """
    def __init__(self, size=0):
        """
        to initialize square
        Args: size
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
        area of square
        """
        return self.__size * self.__size

    def my_print(self):
        """
        square with the character #
        """
        if self.__size == 0:
            print()
        for i in range(self.__size):
            print("#" * self.__size)
