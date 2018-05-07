#!/usr/bin/env python3
"""
Test case for the Queue class.
"""
import os
import sys
import unittest

# Add the /Queues directory containing queues.py
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from queues import Queue


class QueueTestCase(unittest.TestCase):
    """Tests the functionality of the Queue class."""
    def setUp(self):
        """
        Create a Queue and a list of objects for use in all the test methods.
        """
        self.queue = Queue()
        self.objects = [5.4, True, "car"]

        # Add objects to the queue
        for object in self.objects:
            self.queue.enqueue(object)

    def test_enqueue(self):
        """Tests whether the objects are properly stored within the Queue."""
        self.assertEqual(self.queue.items, list(reversed(self.objects)))

    def test_dequeue(self):
        """Tests whether objects are properly removed from the Queue."""
        object = self.queue.dequeue()
        self.assertNotIn(object, self.queue.items)


unittest.main()
