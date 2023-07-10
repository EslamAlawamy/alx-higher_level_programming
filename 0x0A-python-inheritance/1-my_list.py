#!/usr/bin/python3
""" My list Func """


class MyList(list):
    """ class inheritance """
    def print_sorted(self):
        """ function that prints the list,
        but sorted (ascending sort)"""
        print(sorted(list(self)))
