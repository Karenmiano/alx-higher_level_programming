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
        rows = [str(self.print_symbol) * self.__width
                for _ in range(self.__height)]
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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """Compares the area of two rectangles.

        Args:
            rect_1: first rectangle
            rect_2: second rectangle
        Returns:
            returns the largest rectangle, rect_1 if they are equal
        """
        if type(rect_1).__name__ != 'Rectangle':
            raise TypeError("rect_1 must be an instance of Rectangle")
        if type(rect_2).__name__ != 'Rectangle':
            raise TypeError("rect_2 must be an instance of Rectangle")
        area1 = rect_1.area()
        area2 = rect_2.area()
        if area1 == area2 or area1 > area2:
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        """Returns a square"""
        return cls(size, size)