#!/usr/bin/python3
for a in range(97, 123, -1):
    print("{:c}".format(a if a % 2 == 0), end="")
