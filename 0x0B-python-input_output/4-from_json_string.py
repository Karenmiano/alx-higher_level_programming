#!/usr/bin/python3
"""Defines the function from_json_string."""
import json


def from_json_string(my_str):
    """Returns a python object from a json string."""
    return json.loads(my_str)
