#!/usr/bin/python3
"""Defines the function read_file."""


def read_file(filename=""):
    """Reads a file and prints the content to stdout."""
    with open(filename, 'r', encoding="UTF8") as new_file:
        print(new_file.read(), end="")
