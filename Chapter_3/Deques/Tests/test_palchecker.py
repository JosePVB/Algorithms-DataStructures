#!/usr/bin/env python3
import unittest

import Chapter_3.Deques.palchecker as pc


class TestPalChecker(unittest.TestCase):
    palchecker = pc.palchecker
    """
    Tests that the palindrome checker function returns the expected outputs.
    """
    def test_even_character_palindrome(self):
        self.assertEqual(TestPalChecker.palchecker("toot"), True)

    def test_odd_character_palindrome(self):
        self.assertEqual(TestPalChecker.palchecker("radar"), True)

    def test_not_a_palindrome(self):
        self.assertEqual(TestPalChecker.palchecker("false"), False)

    def test_palindrome_with_spaces(self):
        self.assertEqual(TestPalChecker.palchecker("I PREFER PI"), True)


if __name__ == "__main__":
    unittest.main()
