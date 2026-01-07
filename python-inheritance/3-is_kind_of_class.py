#!/usr/bin/python3
"""Defines a function that checks if an object is an instance of a class or inherited."""


def is_kind_of_class(obj, a_class):
    """Return True if obj is instance of a_class (or subclass); otherwise False."""
    return isinstance(obj, a_class)
