#!/usr/bin/env python3
import unittest


import Chapter_3.Deques.deques as deques


class TestDeque(unittest.TestCase):
    """
    Tests the functionality of the Deque class.
        -   Creation from lists.
        -   Creation from genexps.
        -   Creation from non-iterables.

        -   Addition to the right side of the deque.
        -   Addition to the left side of the deque.

        -   * operator.
        -   ** operator.
    """
    def setUp(self):
        """
        Deques and lists used throughout the test cases.
        """
        self.right_appended_deque = deques.Deque()
        self.left_appended_deque = deques.Deque()
        self.items = [1, 2, 3]
        self.additional_items = [4, 5, 6]

        for item in self.items:
            self.right_appended_deque.append_right(item)
            self.left_appended_deque.append_left(item)

    def test_deque_instantiation_from_list(self):
        """
        Test whether a Deque is the same whether each item is appended one at
        a time or passed all at once in a list.
        """
        self.assertEqual(self.right_appended_deque, deques.Deque(self.items))
        self.assertEqual(self.left_appended_deque,
                         deques.Deque(self.items[::-1]))

    def test_deque_instantiation_from_genexp(self):
        """
        Test the creation of a Deque through a generator expression.
        """
        # Test right append
        genexp = (item for item in self.items)
        self.assertEqual(self.right_appended_deque, deques.Deque(genexp))

        # Test left append
        genexp = (item for item in self.items[::-1])
        self.assertEqual(self.left_appended_deque, deques.Deque(genexp))

    def test_deque_raises_for_non_iterable(self):
        """
        Tests that a Deque can not be created from a non iterable.
        """
        with self.assertRaises(TypeError):
            deques.Deque(1)

    def test_deque_addition_to_right(self):
        """
        Tests the result of Deque + iterable
        """
        self.assertEqual(self.right_appended_deque + self.additional_items,
                         deques.Deque(self.items + self.additional_items))
        self.assertEqual(
            self.left_appended_deque + self.additional_items,
            deques.Deque(self.items[::-1] + self.additional_items)
        )

        # Test exception when item is not an iterable.
        with self.assertRaises(TypeError):
            self.left_appended_deque + True

    def test_deque_addition_to_left(self):
        """
        Tests the result of iterable + Deque
        """
        self.assertEqual(self.additional_items + self.right_appended_deque,
                         deques.Deque(self.additional_items + self.items))
        self.assertEqual(
            self.additional_items + self.left_appended_deque,
            deques.Deque(self.additional_items + self.items[::-1])
        )

        # Test exception when item is not an iterable.
        with self.assertRaises(TypeError):
            3 + self.right_appended_deque

    def test_deque__mul__(self):
        """
        Tests the result of Deque * n
        """
        self.assertEqual(self.right_appended_deque * 2,
                         deques.Deque(self.items * 2))
        self.assertEqual(self.left_appended_deque * 3,
                         deques.Deque(self.items[::-1] * 3))

    def test_deque__pow__(self):
        """
        Tests the result of Deque ** n
        """
        self.assertEqual(
            self.right_appended_deque ** 2,
            deques.Deque([num for num in self.items for _ in range(2)])
        )
        self.assertEqual(
            self.left_appended_deque ** 4,
            deques.Deque((num for num in self.items[::-1] for _ in range(4)))
        )


if __name__ == "__main__":
    unittest.main()
