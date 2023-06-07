#!/usr/bin/python3
for a in range(97,123,-1):
    if a % 2 == 0:
        print("{:c}".format(a), end="")
