#!/usr/bin/python3
""" the main class module """


class Square:
    """ the class of square """
    def __init__(self, size=0):
        """
        init function to initialize the square
        Args: size(int): the size of the square
        """
        if type(size) != int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
