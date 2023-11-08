"""String object."""

from __future__ import annotations

from pointless_adding.objects.object import Object

class StringObject(Object):
    """
    An object that represents a string.
    """
    def __init__(self, value):
        """
        Parameters
        ----------
        value : str
            The string value.
        """
        self.value = str(value)

    def __repr__(self):
        return f"StringObject({self.value})"
