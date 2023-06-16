#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0
    s = 0
    w = 0
    for score, weight in my_list:
        s = s + score * weight
        w = w + weight

    return s / w
