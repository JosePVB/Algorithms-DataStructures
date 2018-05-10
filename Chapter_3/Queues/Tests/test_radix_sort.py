#!/usr/bin/env python
import unittest

import Chapter_3.Queues.radix_sort as radix_sort


class TestRadixSort(unittest.TestCase):
    """
    Verifies that the radix sort function works as intended.
    """
    def test_distinct_integers(self):
        """
        Test whether the result of the function is the same as the built-in
        sorted() function for a list of distinct integers.
        """
        self.integers = [2, 108, 13, 1, 99, 317]
        self.assertEqual(radix_sort.radix_sort(self.integers),
                         sorted(self.integers))
        self.assertEqual(radix_sort.radix_sort(self.integers, reverse=True),
                         sorted(self.integers, reverse=True))

    def test_duplicate_integers(self):
        """
        Test whether the result of the function is the same as the built-in
        sorted() function for a list that contains duplicate integers.
        """
        self.integers = [3, 14, 3, 95, 203, 203, 11]
        self.assertEqual(radix_sort.radix_sort(self.integers),
                         sorted(self.integers))
        self.assertEqual(radix_sort.radix_sort(self.integers, reverse=True),
                         sorted(self.integers, reverse=True))


if __name__ == "__main__":
    unittest.main()
