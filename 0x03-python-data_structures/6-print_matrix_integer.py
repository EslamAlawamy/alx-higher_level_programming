#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for f in matrix:
            for s in f:
                print("{:d}".format(s), end=" ")
            print()
