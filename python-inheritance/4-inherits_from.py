#!/usr/bin/python3
"""Defines a function that checks if an object inherits from a class (not same class)."""


def inherits_from(obj, a_class):
    """
    Return True if obj is an instance of a subclass of a_class (directly/indirectly),
    but not an instance of a_class itself.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
