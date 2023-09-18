#!/usr/bin/python3
"""Defines my base class."""
import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns a json string of a list of dictionaries."""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes a list of cbjects to a file."""
        file_name = cls.__name__ + ".json"
        with open(file_name, "w", encoding="UTF8") as json_file:
            if list_objs is None:
                json_file.write("[]")
            else:
                l_dicts = [obj.to_dictionary() for obj in list_objs]
                json_file.write(Base.to_json_string(l_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Returns the python list representation of json_string."""
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)
