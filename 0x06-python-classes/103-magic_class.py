#!/usr/bin/python3
""" the module """
import math

class MagicClass:
    """ the class  """
    def __init__(self, radius):
        """ Args: is radius"""
        self.__radius = 0
        if type(radius) is not (int, float):
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        return self.__radius ** 2 * math.pi

    def circumference(self):
        return 2 * math.pi * self.__radius