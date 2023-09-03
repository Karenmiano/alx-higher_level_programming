#!/usr/bin/python3

"""Defines the function say_my_name()"""


def say_my_name(first_name, last_name=""):
    """Prints names.

    Args:
       first_name: first name to print
       last_name: last name to print
    Raises:
       TypeError: when input is not a string.
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    if type(last_name) is not str:
        raise TypeError("last_name must be a string")
    print("My name is {} {}".format(first_name, last_name))
