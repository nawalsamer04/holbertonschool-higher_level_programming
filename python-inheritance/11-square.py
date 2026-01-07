#!/usr/bin/python3
"""Defines a Square class that inherits from Rectangle."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class (inherits from Rectangle)."""

    def __init__(self, size):
        """Initialize a square with a validated size."""
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """Return the string representation of the square."""
        return "[Square] {}/{}".format(self.__size, self.__size)
