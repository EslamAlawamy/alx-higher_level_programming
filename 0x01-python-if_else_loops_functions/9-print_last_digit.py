#!/usr/bin/python3
def print_last_digit(number):
    if number > -1:
        last = number % 10
    elif number < 1:
        last = number % -10
    return (last)
