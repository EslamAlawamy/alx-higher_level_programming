#!/usr/bin/python3
""" Load, add, save """
import sys


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').\
        load_from_json_file

try:
    j_obj = load_from_json_file("add_item.json")
    j_obj += sys.argv[1:]
    save_to_json_file(j_obj, "add_item.json")
except FileNotFoundError:
    save_to_json_file(sys.argv[1:], "add_item.json")
