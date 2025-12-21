#!/usr/bin/python3
"""Defines a Student class with filtered JSON output."""


class Student:
    """Student class."""

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Return dictionary representation of a Student instance.

        If attrs is a list of strings, return only matching attributes.
        """
        if (isinstance(attrs, list) and
                all(isinstance(x, str) for x in attrs)):
            result = {}
            for name in attrs:
                if hasattr(self, name):
                    result[name] = getattr(self, name)
            return result
        return self.__dict__
