"""Object."""

from __future__ import annotations
from abc import ABC, abstractmethod

class Object(ABC):
    """
    Generic object class.
    """
    @abstractmethod
    def __init__(self, value):
        """
        Initialize the object.
        """

    @abstractmethod
    def __repr__(self):
        """
        Return the string representation of the object.
        """

    def prn(self):
        """
        Print the object.
        """
        print(repr(self))

    def add_to(self, other: 'Object', adder: 'Adder') -> 'Adder':
        """
        Add this object to another object.

        Returns:
            Adder object.
        """
        return adder.add(self, other)
