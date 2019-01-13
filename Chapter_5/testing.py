#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest
import random
import sys
import os

# Append the directory of this script to be able to import the
# search 
sys.path.append(os.path.dirname(os.path.realpath(__file__)))

from search import sequential_search, binary_search, Map
from sorting import bubble_sort, selection_sort, insertion_sort, shell_sort, merge_sort


class TestSearchAlgorithmMixin:

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
  
    def test_first_item(self):
        self.assertTrue(self.algorithm(self.first, self.values))
    
    def test_last_item(self):
        self.assertTrue(self.algorithm(self.last, self.values))
    
    def test_value_present(self):
        self.assertTrue(self.algorithm(self.value_present, self.values))
    
    def test_value_not_present(self):
        self.assertFalse(self.algorithm(self.value_not_present, self.values))


class TestSortingAlgorithmMixin:

    def setUp(self):
        self.positive_list, self.ordered_positive_list = (
            list(range(10)), list(range(10))
        )
        self.negative_list, self.ordered_negative_list = (
            list(range(-53, 0, -1)), list(range(-53, 0, -1))
        )
        self.mixed_list, self.ordered_mixed_list = (
            list(range(-42, 75)), list(range(-42, 75))
        )

        random.shuffle(self.positive_list)
        random.shuffle(self.negative_list)
        random.shuffle(self.mixed_list)
    
    def test_positive_list(self):
        """
        Test the algorithm for positive numbers.
        """
        self.positive_list = self.algorithm(self.positive_list)
        self.assertEqual(self.positive_list, self.ordered_positive_list)
    
    def test_negative_list(self):
        """
        Test the algorithm for negative numbers.
        """
        self.negative_list = self.algorithm(self.negative_list)
        self.assertEqual(self.negative_list, self.ordered_negative_list)
    
    def test_mixed_list(self):
        """
        Test the algorithm for mixed list of numbers, both postive and
        negative.
        """
        self.mixed_list = self.algorithm(self.mixed_list)
        self.assertEqual(self.mixed_list, self.ordered_mixed_list)
    
    def test_empty_list(self):
        """
        Test that no error is raised if trying to sort an empty list.
        """
        self.assertEqual([], self.algorithm([]))


class TestMapADT(unittest.TestCase):

    def setUp(self):
        self.map = Map()
        self.slots = [None for _ in range(self.map.size)]
        self.data = [None for _ in range(self.map.size)]
    
    def test_hashfunction(self):
        key = 21
        hash_value = key % self.map.size
        self.assertEqual(self.map.hashfunction(key), hash_value)
    
    def test_rehash(self):
        key = 5
        hash_value = (key + 1) % self.map.size
        self.assertEqual(self.map.rehash(key), hash_value)
    
    def test_put_slots(self):
        """
        Tests that the key is stored at the expected index.
        """
        key, value = 54, "cat"
        self.slots[self.map.hashfunction(54)] = key
        self.map.put(key, value)
        self.assertEqual(self.map.slots, self.slots)
    
    def test_put_data(self):
        """
        Tests that the value is stored at the expected index.
        """
        key, value = 54, "cat"
        self.data[self.map.hashfunction(54)] = value
        self.map.put(key, value)
        self.assertEqual(self.map.data, self.data)
    
    def test_setitem_slots(self):
        """
        Tests that the key is stored at the expected index when
        __setitem__ is used.
        """
        key, value = 54, "cat"
        self.slots[self.map.hashfunction(54)] = key
        self.map[key] = value
        self.assertEqual(self.map.slots, self.slots)

    def test_setitem_data(self):
        """
        Tests that the value is stored at the expected index when
        __setitem__ is used.
        """
        key, value = 54, "cat"
        self.data[self.map.hashfunction(54)] = value
        self.map[key] = value
        self.assertEqual(self.map.data, self.data)
    
    def test_get_existing_value(self):
        key, value = 20, "chicken"
        self.map[key] = value
        self.assertEqual(self.map.get(key), value)
    
    def test_getitem_existing_value(self):
        key, value = 20, "chicken"
        self.map[key] = value
        self.assertEqual(self.map[key], value)
    
    def test_getitem_raises_keyerror_if_not_existing_value(self):
        key, value = 20, "chicken"
        self.map[key] = value
        with self.assertRaises(KeyError):
            self.map[key+1]
    
    def test_get_returns_default_if_not_existing_value(self):
        key, value = 20, "chicken"
        self.map[key] = value
        # key + 1 is not in the hash table.
        self.assertEqual(self.map.get(key+1), None)
    
    def test_get_returns_provided_default_if_not_existing_value(self):
        key, value = 20, "chicken"
        default = 'my_desired_default'
        self.map[key] = value
        self.assertEqual(self.map.get(key+1, default), default)
    
    def test_values_stored_in_hash_collision(self):
        key, value = 20, "chicken"
        collision_key, collision_value = (key - self.map.size), "dog"
        self.map[key] = value
        self.map[collision_key] = collision_value
        self.assertEqual(self.map.get(key), value)
        self.assertEqual(self.map.get(collision_key), collision_value)


class TestSequentialSearch(TestSearchAlgorithmMixin, unittest.TestCase):
    
    @staticmethod
    def algorithm(*args, **kwargs):
        return sequential_search(*args, **kwargs)


class TestBinarySeach(TestSearchAlgorithmMixin, unittest.TestCase):
    
    @staticmethod
    def algorithm(*args, **kwargs):
        return binary_search(*args, **kwargs)


class TestBubbleSort(TestSortingAlgorithmMixin, unittest.TestCase):
    
    @staticmethod
    def algorithm(*args, **kwargs):
        return bubble_sort(*args, **kwargs)


class TestSelectionSort(TestSortingAlgorithmMixin, unittest.TestCase):

    @staticmethod
    def algorithm(*args, **kwargs):
        return selection_sort(*args, **kwargs)


class TestInsertionSort(TestSortingAlgorithmMixin, unittest.TestCase):

    @staticmethod
    def algorithm(*args, **kwargs):
        return insertion_sort(*args, **kwargs)
    
    def setUp(self):
        super().setUp()
        self.list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
    
    def test_insertion_sort_with_gap(self):
        gap = 3
        self.list = self.algorithm(self.list, gap=gap)
        self.assertEqual([17, 26, 93, 44, 77, 31, 54, 55, 20], self.list)
    
    def test_insertion_sort_with_gap_and_non_zero_starting_index(self):
        gap = 3
        starting_index = 1
        self.list = self.algorithm(
            self.list,
            starting_index=starting_index,
            gap=gap
        )
        self.assertEqual([54, 26, 93, 17, 55, 31, 44, 77, 20], self.list)


class TestShellSort(TestSortingAlgorithmMixin, unittest.TestCase):
    
    @staticmethod
    def algorithm(*args, **kwargs):
        return shell_sort(*args, **kwargs)
    
class TestMergeSort(TestSortingAlgorithmMixin, unittest.TestCase):

    @staticmethod
    def algorithm(*args, **kwargs):
        return merge_sort(*args, **kwargs)



if __name__ == "__main__":
    unittest.main()
