#!/usr/bin/python3
"""
Defines a class MyList that inherits from list
"""


class MyList(list):
    """
    Custom list class with a method to print sorted list
    """

    def print_sorted(self):
        """
        Prints the list sorted in ascending order
        """
        print(sorted(self))
