#!/usr/bin/python3
"""Defines a function that checks class or inherited class."""


def is_kind_of_class(obj, a_class):
    """Return True if obj is instance of a_class or its subclasses."""
    return isinstance(obj, a_class)

