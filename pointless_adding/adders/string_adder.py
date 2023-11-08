"""String adder."""

from pointless_adding.adders.adder import Adder
from pointless_adding.objects.string_object import StringObject

class StringAdder(Adder):
    """
    Adder for strings.
    """
    def add(self, a: StringObject, b: StringObject) -> StringObject:
        """
        Add two strings.
        """
        if int(a.value) and int(b.value):
            return int(a.value) + int(b.value)
        return a.value + b.value

    def add_three(self, a: StringObject, b: StringObject, c: StringObject) -> StringObject:
        """
        Add three strings.
        """
        first_sum = self.add(a, b)
        return self.add(first_sum, c)
