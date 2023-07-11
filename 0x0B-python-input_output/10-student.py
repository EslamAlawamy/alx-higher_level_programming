#!/usr/bin/python3
""" Student to JSON with filter """


class Student:
    """ student class """
    def __init__(self, first_name, last_name, age):
        """ initialize """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        that retrieves a dictionary
        representation of a Student
        """
        if attrs is None or type(attrs) is not list:
            return self.__dict__
        
        return {attr: getattr(self, attr) for attr in attrs if hasattr(self, attr)}
