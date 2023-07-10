#!/usr/bin/python3
""" Text indentation """


def text_indentation(text):
    """
    Return with indentation
    Args is text
    """
    if type(text) is not str:
        raise TypeError("text must be a string")
    new_text = (text.replace(".", ".\n\n").replace("?", "?\n\n")
                .replace(":", ":\n\n"))
    for i in range(len(text)):
        new_text = new_text.replace("\n ", "\n")
    print(new_text, end="")
