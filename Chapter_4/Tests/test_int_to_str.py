#!/usr/bin/env python3

import unittest

import Chapter_4.recursive_integer_to_string as int_to_str


class TestIntToStr(unittest.TestCase):
    """
    Tests for the int_to_str function.

    Methods
    -------
    test_to_binary
        Test integer conversion to binary base.
    test_to_octal
        Test integer conversion to octal base.
    test_to_hexadecimal
        Test integer conversion to hexadecimal base.
    """
    def test_to_binary(self):
        """Compare the returned binary string to the actual value."""
        self.assertEqual(int_to_str.int_to_str(42, 2), "101010")

    def test_to_octal(self):
        """Compare the returned octal string to the actual value."""
        self.assertEqual(int_to_str.int_to_str(1990, 8), "3706")

    def test_to_hexadecimal(self):
        """Compare the return hexadecimal string to the actual value."""
        self.assertEqual(int_to_str.int_to_str(2033, 16), "7F1")

if __name__ == "__main__":
    unittest.main()

