"""Adder."""

from __future__ import annotations

from abc import ABC, abstractmethod

class Adder(ABC):
    """
    Generic adder class.
    """
    def __init__(self):
        """
        Initialize the adder.
        """

    @abstractmethod
    def add(self, a: 'Object', b: 'Object') -> 'Object':
        """
        Add two objects.

        Returns:
            Sum of the two objects. Same type as the objects.
        """

    @abstractmethod
    def add_three(self, a: 'Object', b: 'Object', c: 'Object') -> 'Object':
        """
        Add three objects
        """
