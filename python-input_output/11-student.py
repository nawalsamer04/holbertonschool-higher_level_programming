#!/usr/bin/python3
"""Defines a Student class with JSON serialization/deserialization."""


class Student:
    """Student class."""

    def __init__(self, first_name, last_name, age):
        """Initialize a Student."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieve a dictionary representation of a Student.

        If attrs is a list of strings, only return those attributes
        that exist in the instance.
        """
        if isinstance(attrs, list) and all(isinstance(x, str) for x in attrs):
            result = {}
            for name in attrs:
                if hasattr(self, name):
                    result[name] = getattr(self, name)
            return result
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the Student instance from a dictionary."""
        for key, value in json.items():
            setattr(self, key, value)
