#!/usr/bin/python3
def uppercase(str):
    for n in str:
        if ord(n) > 96 and ord(n) < 123:
            print("{:c}".format(ord(n) - 32), end="")
        else:
            print(n, end="")
    print()
