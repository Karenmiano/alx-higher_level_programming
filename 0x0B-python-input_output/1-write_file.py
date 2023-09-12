#!/usr/bin/python3
"""Defines the function write_file."""


def write_file(filename="", text=""):
    """Writes a string to a text file.

    Returns:
        returns the number of characters written.
    """

    with open(filename, 'w', encoding="UTF8") as file_w:
        nb_chars = file_w.write(text)
    return nb_chars
