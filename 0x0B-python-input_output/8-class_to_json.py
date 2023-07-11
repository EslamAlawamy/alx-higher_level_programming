#!/usr/bin/pyhon3
""" Class to JSON """
import json


def class_to_json(obj):
    """ returns the dictionary description """
    return obj.__dict__
