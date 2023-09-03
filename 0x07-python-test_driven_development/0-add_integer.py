#!/usr/bin/python3
"""Defines a function that adds numbers"""


def add_integer(a, b=98):
    """Returns the sum of a and b rounded to two decimal places.

    Floats are casted to ints before addition.

    Raises:
      TypeError: if either a or b is not a number
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
