"""Integer adder."""

from pointless_adding.adders.adder import Adder
from pointless_adding.objects.int_object import IntObject

class IntAdder(Adder):
    """
    Adder for two integers.
    """
    def add(self, a: IntObject, b: IntObject) -> IntObject:
        """
        Add two integers.
        """
        return IntObject(a.value + b.value)

    def add_three(self, a: IntObject, b: IntObject, c: IntObject) -> IntObject:
        """
        Add three integers.
        """
        return IntObject(a.value + b.value + c.value)
