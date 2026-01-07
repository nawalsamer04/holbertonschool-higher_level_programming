#!/usr/bin/python3
"""Defines a function that adds a new attribute if possible."""


def add_attribute(obj, name, value):
    """Add attribute to obj if possible, otherwise raise TypeError."""
    if hasattr(obj, "__dict__"):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
