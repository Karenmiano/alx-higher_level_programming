#!/usr/bin/python3
"""Defines a class Square."""

from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines a square object."""
    def __init__(self, size, x=0, y=0, id=None):
        """Initializes a square object.

        Args:
            size: size of one side
            x: x coordinate of the square
            y: y coordinate of the square
            id: identity of the square object
        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns an informative string on the square object."""
        return "[Square] ({}) {}/{} - {}".format(self.id,
                                                 self.x, self.y,
                                                 self.width)
