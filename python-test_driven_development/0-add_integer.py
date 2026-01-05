#!/usr/bin/python3
"""Module that provides a function to add two numbers safely."""


def add_integer(a, b=98):
    """Return the integer addition of a and b.

    a and b must be integers or floats, otherwise a TypeError is raised.
    Floats are first cast to integers.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
