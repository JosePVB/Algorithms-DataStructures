#!/usr/bin/env python3


class Queue:
    """
    A queue data structure based upon a Python list. Objects are added to the
    queue through the left and leave the queue through the right. Therefore
    additions to the queue are O(n) while removals are O(1).
    """
    def __init__(self):
        """Constructor for the Queue class."""
        self.items = []

    def enqueue(self, item):
        """
        Adds item to the Queue instance.

        Variables
        ---------
        item
        """
        self.items.insert(0, item)

    def dequeue(self):
        """Removes and returns the last item in the Queue."""
        return self.items.pop()

    def is_empty(self):
        """Returns True if the Queue is empty."""
        return self.items == []

    def size(self):
        """Returns the number of objects currently in the Queue."""
        return len(self.items)
