#!/usr/bin/python3
""" Divide a matrix """


def matrix_divided(matrix, div):
    """
    Returns: new matrix (list of lists)
        Arges:
            matrix: (list of lists)
            div: int
    """
    error = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list:
        raise TypeError(error)

