#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if matrix:
        for f in range(len(matrix)):
            for s in range(len(matrix[f])):
                print("{:d}".format(matrix[f][s]), end=" ")
            print()
