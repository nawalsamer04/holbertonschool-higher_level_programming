#!/usr/bin/python3
"""
Module that provides class_to_json function.
"""


def class_to_json(obj):
    """
    Returns the dictionary description of a simple data structure
    for JSON serialization of an object.
    """
    return obj.__dict__.copy()
