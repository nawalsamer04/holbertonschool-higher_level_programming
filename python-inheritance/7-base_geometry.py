#!/usr/bin/python3
"""Defines BaseGeometry with area() and integer_validator()."""


class BaseGeometry:
    """Base class for geometry objects."""

    def area(self):
        """Raise an Exception because area is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is a proper integer (> 0)."""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
