#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    my_new = []
    for key, val in a_dictionary.items():
        if val == value:
            my_new.append(key)
    for key in my_new:
        del a_dictionary[key]
    return a_dictionary
