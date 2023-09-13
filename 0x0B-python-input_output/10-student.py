#!/usr/bin/python3
"""Defines a student class."""


class Student:
    """Represents a student."""

    def __init__(self, first_name, last_name, age):
        """Creates a new student.

        Args:
            first_name: first name of the student.
            last_name: last name of the student.
            age: age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns a dictionary representation of an object."""
        dictionary = self.__dict__
        new_dict = {}
        if isinstance(attrs, list) and all(isinstance(x, str) for x in attrs):
            for key in attrs:
                if key in dictionary:
                    new_dict[key] = dictionary[key]
            return new_dict
        else:
            return self.__dict__
