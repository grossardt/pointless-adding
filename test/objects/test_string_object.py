
""" Test String Object """

import unittest
from ddt import ddt

from pointless_adding.objects import StringObject

@ddt
class TestStringObject(unittest.TestCase):
    """Test String Object"""

    def test_string_object_init(self):
        """Test initialization."""
        string_object = StringObject("Hello")
        self.assertEqual(string_object.value, "Hello")

    def test_string_object_print(self):
        """Test printing."""
        string_object = StringObject("Hello")
        self.assertEqual(string_object.prn(), "StringObject(Hello)")

if __name__ == "__main__":
    unittest.main()
