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

    def to_json(self):
        """Returns a dictionary representation of an object."""
        return self.__dict__
