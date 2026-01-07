#!/usr/bin/python3
"""Defines BaseGeometry with area and integer validation."""


class BaseGeometry:
    """BaseGeometry with area and integer validation."""

    def area(self):
        """Raise an Exception because area is not implemented."""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is an int > 0.

        Args:
            name (str): the name of the value
            value (int): the value to validate

        Raises:
            TypeError: if value is not an integer
            ValueError: if value <= 0
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
