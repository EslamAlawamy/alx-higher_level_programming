#!/usr/bin/python3
""" Load, add, save """
import sys


save_to_json_file = __import__('5-save_to_json_file.py').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file.py').\
        load_from_json_file

filename = "add_item.json"

try:
    j_obj = load_from_json_file(filename)
    j_obj += sys.argv[1:]
    save_to_json_file(j_obj, filename)
except FileNotFoundError:
    save_to_json_file(sys.argv[1:], filename)
