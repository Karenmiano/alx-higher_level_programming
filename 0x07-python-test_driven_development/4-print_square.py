#!/usr/bin/python3

"""Defines function that prints a square"""


def print_square(size):
    """Prints a square using '#'.

    Args:
        size(int): size of square
    Raises:
        TypeError: when size is not an integer
        ValueError: when size is less than zero
    """

    if type(size) != int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for row in range(size):
        print("#" * size)
