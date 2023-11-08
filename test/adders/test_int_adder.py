
""" Test Int Adder """

import unittest
from ddt import ddt

from pointless_adding.objects.int_object import IntObject
from pointless_adding.adders.int_adder import IntAdder

@ddt
class TestIntAdder(unittest.TestCase):
    """Test Int Adder"""

    def test_int_adder(self):
        """Test."""
        a = IntObject("2")
        b = IntObject("3")
        int_adder = IntAdder()
        self.assertEqual(int_adder.add(a,b), 5)

if __name__ == "__main__":
    unittest.main()
