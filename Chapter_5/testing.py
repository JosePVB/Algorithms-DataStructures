#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
import sys
import os

# Append the directory of this script to be able to import the
# search 
sys.path.append(os.path.dirname(os.path.realpath(__file__)))

from search import sequential_search, binary_search


class TestSearchAlgorithms(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        # The list of values to search.
        cls.values = [i for i in range(-5000, 5001)]
    
    def setUp(self):

        # The value for which the algorithms should return True.
        self.first = -5000
        self.last = 5000
        self.value_present = 93

        # Value for which the algorithms should return False.
        self.value_not_present = -6000
  
    def test_sequential_search_first_item(self):
        self.assertTrue(sequential_search(self.first, self.values))
    
    def test_sequential_search_last_item(self):
        self.assertTrue(sequential_search(self.last, self.values))
    
    def test_sequential_search_value_present(self):
        self.assertTrue(
            sequential_search(self.value_present, self.values)
        )
    
    def test_sequential_search_value_not_present(self):
        self.assertFalse(
            sequential_search(self.value_not_present, self.values)
        )
    
    def test_binary_search_first_item(self):
        self.assertTrue(binary_search(self.first, self.values))
    
    def test_binary_search_last_item(self):
        self.assertTrue(binary_search(self.last, self.values))
    
    def test_binary_search_value_present(self):
        self.assertTrue(
            binary_search(self.value_present, self.values)
        )
    
    def test_binary_search_value_not_present(self):
        self.assertFalse(
            binary_search(self.value_not_present, self.values)
        )

if __name__ == "__main__":
    unittest.main()
