#!/usr/bin/python3
""" And now, the Square! """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ class Square that inherits Rectangle """
    def __init__(self, size, x=0, y=0, id=None):
        """ initialize func """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """ return string """
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """ size getter """
        return self.width

    @size.setter
    def size(self, value):
        """ size setter """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """ assigns attributes """
        if args:
            attrs = ['id', 'size', 'x', 'y']
            for i, value in enumerate(args):
                setattr(self, attrs[i], value)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """ returns the dictionary representation of a Square """
        return {
            'id': self.id,
            'size': self.width,
            'x': self.x,
            'y': self.y
        }
