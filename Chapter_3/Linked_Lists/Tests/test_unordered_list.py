#!/usr/bin/env python3
"""
Tests the functionality of the unordered linked list.
"""
import unittest

from ddt import ddt, data

import Chapter_3.Linked_Lists.unordered_list as ul


@ddt
class TestUnorderedList(unittest.TestCase):

    def setUp(self):
        """
        Creates a non-empty and an empty UnorderedList instance.
        Creates a list equivalent to test indexing and slicing.
        """
        self.unordered_list = ul.UnorderedList()
        self.num_elements = 25
        for i in range(self.num_elements):
            self.unordered_list.add(i)

        self.empty_unordered_list = ul.UnorderedList()

        self.list_equivalent = list(reversed(range(self.num_elements)))

    def test_length_of_linked_list(self):
        """Test the __len__() method."""
        self.assertEqual(len(self.unordered_list), self.num_elements)

    def test_length_of_empty_linked_list(self):
        self.assertEqual(len(self.empty_unordered_list), 0)

    def test_boolean_result_of_non_empty_linked_list(self):
        self.assertTrue(self.unordered_list)

    def test_boolean_result_of_empty_linked_list(self):
        self.assertFalse(self.empty_unordered_list)

    def test_linked_list_contains(self):
        """Test the __contains__() method."""
        self.assertTrue(self.num_elements // 2 in self.unordered_list)

    def test_linked_list_does_not_contain(self):
        self.assertFalse(self.num_elements * 2 in self.unordered_list)

    def test_equality_between_different_instances_of_linked_lists(self):
        """Test the __eq__() method."""
        another_linked_list = ul.UnorderedList()
        for i in range(self.num_elements):
           another_linked_list.add(i)
        self.assertEqual(self.unordered_list, another_linked_list)

    def test_positive_indexing_of_linked_list(self):
        for i in range(self.num_elements):
            actual_item = self.unordered_list[i]
            expected_item = self.list_equivalent[i]
            self.assertEqual(actual_item, expected_item)

    def test_negative_indexing_of_linked_list(self):
        for i in range(-self.num_elements, 0, -1):
             actual_item = self.unordered_list[i]
             expected_item = self.list_equivalent[i]
             self.assertEqual(actual_item, expected_item)

    def test_linked_list_throws_IndexError_for_index_out_of_range(self):
        # Test index out of range.
        with self.assertRaises(IndexError):
            self.unordered_list[len(self.unordered_list)]

    @data(
        slice(3, 8),  # 1) Test slice with no step.
        slice(3, 7, 2),  # 2) Test slice with an even step.
        slice(1, 19, 3),  # 3) Test slice with an odd step.
        slice(16, 4, -1),  # 4) Test a reverse slice.
        slice(-4, 1, -4),  # 5) Test a reverse slice with an even step.
        slice(22, 3, -5),  # 6) Test a reverse slice with an odd step.
        slice(22, 3, 5),  # 7) Test an invalid slice.
        slice(None),  # 8) Test an empty slice, [:].
        slice(None, None, -1)  # 9) Test a reverse empty slice, [::-1].
    )
    def test_slice_of_unordered_list(self, slice_object):
        """Test the slicing of a linked list"""
        sliced_list = [
            node.get_item()
            for node in self.unordered_list[slice_object]
        ]
        self.assertEqual(sliced_list, self.list_equivalent[slice_object])


if __name__ == "__main__":
    unittest.main()

