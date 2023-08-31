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

    @property
    def size(self):
        """Returns the size of a square"""

        return self.__size

    @size.setter
    def size(self, value):
        """Sets the value of a square

        Args:
            value(int): size of square
        """
        if isinstance(value, int) is not True:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Returns the area of a square."""
        return (self.__size ** 2)
