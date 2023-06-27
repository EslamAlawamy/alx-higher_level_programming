#!/usr/bin/python3
""" the module """


class Square:
    """ the class """
    def __init__(self, size=0, position=(0, 0)):
        """
        initialize the square
        Args: size, position
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        size getter
        """
        return self.__size

    @size.setter
    def size(self, value):
        """ size setter """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """ positon getter """
        return self.__position

    @position.setter
    def position(self, value):
        """ psition setter """
        if type(value) != tuple or len(value) != 2 or not
                all(isinstance(num, int) for num in value) or
                not all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """ the area """
        return self.__size ** 2

    def my_print(self):
        """ print the # """
        if self.__size == 0:
            print()
        else:
            for i in range(self.__position[1]):
                print()
            for i in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
