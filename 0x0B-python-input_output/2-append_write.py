#!/usr/bin/python3
"""Defines the function append_write."""


def append_write(filename="", text=""):
    """Appends a string to a text file.

    Returns:
        The number of characters apppended.
    """
    with open(filename, 'a', encoding="UTF8") as file_a:
        nb_chars = file_a.write(text)
        return nb_chars
