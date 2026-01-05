#!/usr/bin/python3
"""
Module that prints a formatted name.
"""


def say_my_name(first_name, last_name=""):
    """
    Print: My name is <first name> <last name>

    Args:
        first_name (str): First name.
        last_name (str): Last name (optional).

    Raises:
        TypeError: If first_name or last_name is not a string.
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name))
