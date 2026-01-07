#!/usr/bin/python3
"""Defines a rebel integer class MyInt."""


class MyInt(int):
    """MyInt inverts == and !=."""

    def __eq__(self, other):
        """Invert equality."""
        return int(self) != other

    def __ne__(self, other):
        """Invert inequality."""
        return int(self) == other
