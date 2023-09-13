#!/usr/bin/python3
"""Defines the function class_to_json."""


def class_to_json(obj):
    """Returns a dictionary description of an object."""

    return obj.__dict__
