#!/usr/bin/python3

"""Defines a class Square"""


class Square:
    """Represents a square."""

    def __init__(self, size=0, position=(0,0)):
        """Initializes a new square.

        Args:
            size(int): length of one side.
        """
        if isinstance(size, int) is not True:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.__position = position

    @property
    def position(self):

        return self.__position

    @position.setter
    def position(self, value):
        if not isinstance(value, tuple):
            raise TypeError("position must be a tuple of 2 positive integers")
        elif len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        elif value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

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

    def my_print(self):
        """Prints a visual square using #"""

        if self.__size == 0:
            print()
        else:
            for width in range(self.__size):
                print("\n" * self.__position[1], end="")
                print(" " * self.__position[0] + "#" * self.__size)

    def area(self):
        """Returns the area of a square."""
        return (self.__size ** i2)
