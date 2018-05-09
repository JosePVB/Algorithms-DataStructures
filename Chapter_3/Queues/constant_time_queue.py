#!/usr/bin/env python3
"""
Implements a Queue data structure that has O(1) enqueue and amortized constant
time dequeue methods.
"""
from Chapter_3.Stacks import stacks


class Queue():
    """
    Queue is implemented as two stacks, which allows for O(1) enqueue and
    amortized constant time dequeues.
    """
    def __init__(self):
        """Constructor."""
        self._instack = stacks.Stack()
        self._outstack = stacks.Stack()

    def __len__(self):
        return len(self.items)

    def enqueue(self, item):
        """
        The enqueue operation is always a single push, therefore it is
        O(1).
        """
        self._instack.push(item)

    def dequeue(self):
        """
        In the worst case, where self._outstack is empty, the dequeue operation
        is O(n), therefore this operation is amortized constant time.
        """
        if self._outstack.is_empty():
            while not self._instack.is_empty():
                self._outstack.push(self._instack.pop())
        return self._outstack.pop()

    def is_empty(self):
        return self.items == []

    @property
    def items(self):
        return list(reversed(self._instack.items)) + self._outstack.items
