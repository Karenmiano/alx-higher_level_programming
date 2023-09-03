#!/usr/bin/python3

"""Defines a function that divides a matrix"""


def matrix_divided(matrix, div):
    """Divides all elements in a matrix.

    Args:
        matrix(list): a list of lists of integers or floats.
        div(float/int): The divisor
    Raises:
        TypeError: if matrix is not a list of lists and individual
                   elements are non-numbers
        TypeError: if rows are not of the same size
        TypeError: if div is a non-number
        ZeroDivisionError: if div is 0
    Returns:
        A new matrix of elements after division
    """

    type_msg = "matrix must be a matrix (list of lists) of integers/floats"
    if type(matrix) is not list:
        raise TypeError(type_msg)
    for row in matrix:
        if type(row) is not list:
            raise TypeError(type_msg)
    length = len(matrix[0])
    for row in matrix:
        if len(row) != length:
            raise TypeError("Each row of the matrix must have the same size")
    for row in matrix:
        for i in row:
            if type(i) not in [int, float]:
                raise TypeError(type_msg)
    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_matrix = []
    for row in matrix:
        new_row = [round((i / div), 2) for i in row]
        new_matrix.append(new_row)
    return (new_matrix)
