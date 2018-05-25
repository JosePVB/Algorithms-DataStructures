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
        for i in range(-self.num_elements, 0, 1):
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

    def test_append_method_of_linked_list(self):
        value_to_append = 6
        self.unordered_list.append(value_to_append)
        self.list_equivalent.append(value_to_append)
        list_of_values = [
            node.get_item()
            for node in self.unordered_list
        ]
        self.assertEqual(list_of_values, self.list_equivalent)


    def test_index_method_of_linked_list(self):
        """Test the .index(item) method."""
        self.assertEqual(self.unordered_list.index(20), 4)

    def test_index_method_raises_ValueError(self):
        """
        The .index(item) method should raise ValueError if `item` is not
        in the list.
        """
        with self.assertRaises(ValueError):
            self.unordered_list.index(50)

    def test_item_received_from_pop_method(self):
        self.assertEqual(self.unordered_list.pop(), 0)

    def test_length_of_list_is_reduced_by_pop_method(self):
        _ = self.unordered_list.pop()

        predicted_length = self.num_elements - 1
        actual_length = len(self.unordered_list)
        self.assertTrue(actual_length == predicted_length)

    def test_pop_raises_IndexError(self):
        """IndexError should be raised when popping from an empty list."""
        with self.assertRaises(IndexError):
            self.empty_unordered_list.pop()

    def test_pop_list_with_one_item(self):
        other_list = ul.UnorderedList()
        other_list.add(1)
        _ = other_list.pop()
        self.assertEqual(other_list, self.empty_unordered_list)

    def test_insert_in_middle_of_list(self):
        """
        Insert method should work the same as for a normal python list.
        """
        value_to_insert = 6

        # Create a new linked list that will be used for comparison.
        other_list = ul.UnorderedList()
        list_of_nums = [
            num
            for num in range(self.num_elements - 4, self.num_elements)
        ]
        list_of_nums.insert(2, value_to_insert)
        for num in list_of_nums:
            other_list.add(num)

        # Add value in the middle of a linked list.
        self.unordered_list.insert(2, value_to_insert)

        self.assertEqual(self.unordered_list[:5], other_list)

    def test_insert_into_linked_list_with_a_single_node(self):
        """
        Insert method should work the same as for a normal python list.
        """
        value_to_insert = 6

        # Create a new unordered list to compare to.
        test_list = ul.UnorderedList()
        test_list.add(value_to_insert)
        test_list.insert(1, value_to_insert * 2)

        for num in (value_to_insert * 2, value_to_insert):
            self.empty_unordered_list.add(num)
        self.assertEqual(test_list, self.empty_unordered_list)


if __name__ == "__main__":
    unittest.main()

