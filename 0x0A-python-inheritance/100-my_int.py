#!/usr/bin/python3
""" My integer """


class MyInt(int):
    """
    class MyInt that inherits int
    """
    def __eq__(self, value):
        """ equal """
        return int(self) != value

    def __ne__(self, value):
        """ not equal """
        return int(self) == value
