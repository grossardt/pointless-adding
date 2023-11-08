"""Integer Object."""

from __future__ import annotations

from pointless_adding.objects.object import Object

class IntObject(Object):
    """
    An object that represents an integer.
    """
    def __init__(self, value):
        """
        Parameters
        ----------
        value : int
            The integer value.
        """
        self.value = int(value)

    def __repr__(self):
        return f"IntObject({self.value})"
