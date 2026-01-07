#!/usr/bin/python3
"""Defines a MyList class that inherits from list."""


class MyList(list):
    """Custom list that can print itself sorted."""

    def print_sorted(self):
        """Prints a sorted version of the list (ascending)."""
        print(sorted(self))

