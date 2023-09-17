#!/usr/bin/python3
"""Defines my base class."""


class Base:
    """The base class of all other classes.

    Class Attributes:
        __nb_objects: Number of instatiated objects.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes a new object.

        Args:
            id: identity of the new object.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
