#!/usr/bin/python3
def uppercase(str):
    prin = ""
    for n in str:
        if ord(n) > 96 and ord(n) < 123:
            prin += "{:c}".format(ord(n) - 32)
        else:
            prin += n
    print(prin)
