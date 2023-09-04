#!/usr/bin/python3
"""Defines a class Rectangle."""


class Rectangle:
    """Represents a rectangle."""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """Creates a new square.

        Args:
            width: width of rectangle.
            height: height of rectangle.
        """
        self.width = width
        self.height = height

        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Returns the width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of Rectangle.

        Args:
            value: width of Rectangle.
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Returns the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the Rectangle.

        Args:
            value: height of the Rectangle.
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Returns the area of the rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """Returns the perimeter of the rectangle."""
        if self.__height == 0 or self.__width == 0:
            return 0
        self.__perimeter = (self.__width * 2) + (self.__height * 2)
        return (self.__perimeter)

    def __str__(self):
        """Returns a visual string display of the rectangle using #."""
        if self.__height == 0 or self.__width == 0:
            return ("")
        rows = [str(self.print_symbol) * self.__width for _ in range(self.__height)]
        display = "\n".join(rows)
        return (display)

    def __repr__(self):
        """Returns a formal representation of our rectangle"""
        class_name = type(self).__name__
        return f"{class_name}({self.__width}, {self.__height})"

    def __del__(self):
        """Detects when an instance is being deleted"""
        print("Bye rectangle...")

        Rectangle.number_of_instances -= 1
