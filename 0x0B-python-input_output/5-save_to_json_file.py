#!/usr/bin/python3
"""Defines the function save_to_json_file."""
import json


def save_to_json_file(my_obj, filename):
    """Writes a json string to a text file."""
    with open(filename, 'w', encoding="utf-8") as file:
        json.dump(my_obj, file)
