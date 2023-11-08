
""" Test Int Object """

import unittest
import io
import sys
from ddt import ddt # pylint: disable=import-error

from pointless_adding.objects import IntObject
from pointless_adding.adders import IntAdder

@ddt
class TestIntObject(unittest.TestCase):
    """Test Int Object"""

    def test_int_object_init(self):
        """Test initialization."""
        int_object = IntObject("2")
        self.assertEqual(int_object.value, 2)
        self.assertIsInstance(int_object.value, int)

    def test_int_object_print(self):
        """Test printing."""
        old_stdout = sys.stdout
        sys.stdout = io.TextIOWrapper(io.BytesIO(), sys.stdout.encoding)
        int_object = IntObject("2")
        int_object.prn()
        sys.stdout.seek(0)
        self.assertEqual(sys.stdout.read(), "IntObject(2)\n")
        sys.stdout.close()
        sys.stdout = old_stdout

    def test_int_object_add(self):
        """Test adding."""
        int_object = IntObject("2")
        other_int_object = IntObject("3")
        adder = IntAdder()
        addition_result = int_object.add_to(other_int_object, adder)
        self.assertIsInstance(addition_result, IntObject)
        self.assertEqual(addition_result.value, 5)

if __name__ == "__main__":
    unittest.main()
