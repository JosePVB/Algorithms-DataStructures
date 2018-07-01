#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import unittest

from Chapter_4.fill_water_jugs import WaterJug

class TestWaterJug(unittest.TestCase):
    """
    Tests for the WaterJug class.
    """
    def setUp(self):
        self.small_volume = 3
        self.big_volume = 4

        self.small_jug = WaterJug(self.small_volume)
        self.big_jug = WaterJug(self.big_volume)

    def test_jug_is_empty_when_initialized(self):
        """
        New jug instances should be empty.
        """
        new_jug = WaterJug(25)
        self.assertTrue(new_jug.isempty)

    def test_fill_jug_completely(self):
        """
        Ensure that the .fill() method fills the entire jug.
        """
        self.big_jug.fill()
        self.assertEqual(self.big_jug.content, self.big_volume)

    def test_empty_jug_completely(self):
        """
        Ensure that the .empty() method empties the entire jug.
        """
        self.small_jug.fill()
        self.small_jug.empty()
        self.assertTrue(self.small_jug.isempty)

    def test_empty_small_jug_into_big_jug(self):
        """
        Ensure that the contents of the small jug are placed into the big jug.

        The contents of the big jug should be equal to the volume of the small
        jug.
        """
        self.small_jug.fill()
        self.small_jug.empty(into=self.big_jug)
        self.assertEqual(self.big_jug.content, self.small_volume)

    def test_small_jug_is_empty_after_small_jug_is_emptied_into_big_jug(self):
        """
        Ensure that the small jug is empty after the contents of the small jug
        are placed into the big jug.
        """
        self.small_jug.fill()
        self.small_jug.empty(into=self.big_jug)
        self.assertTrue(self.small_jug.isempty)

    def test_empty_big_jug_into_small_jug(self):
        """
        Ensure that the small jug is full after contents of the big jug are
        placed into the small jug.
        """
        self.big_jug.fill()
        self.big_jug.empty(into=self.small_jug)
        self.assertTrue(self.small_jug.isfull)

    def test_remaining_contents_in_big_jug(self):
        """
        Ensure that the remaining contents in the big jug, after emptying
        its contents into the small jug, is equal to the difference between
        the volume of the two jugs.
        """
        self.big_jug.fill()
        self.big_jug.empty(into=self.small_jug)
        self.assertEqual(
            self.big_jug.content,
            self.big_volume - self.small_volume
        )


if __name__ == "__main__":
    unittest.main()

