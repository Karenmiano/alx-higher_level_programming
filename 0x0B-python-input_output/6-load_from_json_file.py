#!/usr/bin/python3
"""Defines the function load_from_json_file."""
import json


def load_from_json_file(filename):
    """Returns python object from a json file."""
    with open(filename, 'r', encoding="utf-8") as file:
        return json.load(file)
