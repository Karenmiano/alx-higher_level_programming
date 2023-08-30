#!/usr/bin/python3

"""Defines a class Square"""


class Square:
    """Represents a square."""

    def __init__(self, size=0):
        """Initializes a new square.

        Args:
            size(int): length of one side.
        """
        if isinstance(size, int) is not True:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    def area(self):
        """Returns the area of a square."""
        return (self.__size ** 2)
