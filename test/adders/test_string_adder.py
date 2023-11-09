
""" Test String Adder """

import unittest

from pointless_adding.objects.string_object import StringObject
from pointless_adding.adders.string_adder import StringAdder

from test.my_test_case import MyTestCase

class TestStringAdder(MyTestCase):
    """Test Int Adder"""

    def test_simple_strings(self):
        """Test simple strings."""
        a = StringObject("Hello")
        b = StringObject("World")
        string_adder = StringAdder()
        print('before add')
        adder_result = string_adder.add(a,b)
        print('after add')
        self.assertIsInstance(adder_result, StringObject)
        self.assertEqual(adder_result.value, "HelloWorld")

    def test_number_strings(self):
        """Test number strings."""
        a = StringObject("2")
        b = StringObject("3")
        string_adder = StringAdder()
        adder_result = string_adder.add(a,b)
        self.assertIsInstance(adder_result, StringObject)
        self.assertEqual(adder_result.value, "5")

    def test_mixed_strings(self):
        """Test mixed number and non-number strings."""
        a = StringObject("2")
        b = StringObject("Test")
        string_adder = StringAdder()
        adder_result = string_adder.add(a,b)
        self.assertIsInstance(adder_result, StringObject)
        self.assertEqual(adder_result.value, "2Test")


if __name__ == "__main__":
    unittest.main()
