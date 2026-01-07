#!/usr/bin/python3
"""Defines a MyList class that inherits from list."""


class MyList(list):
    """Custom list class with a method to print a sorted list."""

    def print_sorted(self):
        """Prints the list in ascending sorted order."""
        print(sorted(self))

