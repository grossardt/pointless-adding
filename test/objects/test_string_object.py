
""" Test String Object """

import unittest
import io
import sys

from pointless_adding.objects import StringObject

from test.my_test_case import MyTestCase

class TestStringObject(MyTestCase):
    """Test String Object"""

    def test_string_object_init(self):
        """Test initialization."""
        string_object = StringObject("Hello")
        self.assertEqual(string_object.value, "Hello")

    def test_string_object_print(self):
        """Test printing."""
        old_stdout = sys.stdout
        sys.stdout = io.TextIOWrapper(io.BytesIO(), sys.stdout.encoding)
        string_object = StringObject("Hello")
        string_object.prn()
        sys.stdout.seek(0)
        self.assertEqual(sys.stdout.read(), "StringObject(Hello)\n")
        sys.stdout.close()
        sys.stdout = old_stdout

if __name__ == "__main__":
    unittest.main()
