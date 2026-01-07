#!/usr/bin/python3
"""
Task 0: Abstract Animal Class and its Subclasses
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class representing an animal."""

    @abstractmethod
    def sound(self):
        """Return the sound made by the animal."""
        pass


class Dog(Animal):
    """Dog class that implements Animal."""

    def sound(self):
        """Return dog's sound."""
        return "Bark"


class Cat(Animal):
    """Cat class that implements Animal."""

    def sound(self):
        """Return cat's sound."""
        return "Meow"

