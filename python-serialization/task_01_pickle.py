#!/usr/bin/env python3
"""
Task 1 - Pickling Custom Classes
Serialize/deserialize a custom object using pickle.
"""

import pickle


class CustomObject:
    """
    A simple custom object that can be serialized with pickle.

    Attributes:
        name (str): Person name
        age (int): Person age
        is_student (bool): Student status
    """

    def __init__(self, name, age, is_student):
        """Initialize a CustomObject."""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Print the object's attributes in the required format."""
        print("Name: {}".format(self.name))
        print("Age: {}".format(self.age))
        print("Is Student: {}".format(self.is_student))

    def serialize(self, filename):
        """
        Serialize the current instance to a file using pickle.

        Args:
            filename (str): Output filename.
        """
        try:
            with open(filename, "wb") as f:
                pickle.dump(self, f)
        except (OSError, pickle.PickleError):
            pass

    @classmethod
    def deserialize(cls, filename):
        """
        Deserialize a CustomObject instance from a pickle file.

        Args:
            filename (str): Input filename.

        Returns:
            CustomObject | None: Instance if success, otherwise None.
        """
        try:
            with open(filename, "rb") as f:
                obj = pickle.load(f)
            if isinstance(obj, cls):
                return obj
            return None
        except (FileNotFoundError, OSError, pickle.UnpicklingError, EOFError):
            return None

