#!/usr/bin/env python3
"""
Module implements a simple stack data structure.
"""


class Stack():
    """
    The stack data type follows a Last In First Out (LIFO) ordering. This means
    that newer items are near the "top" of the stack, while older items are
    near the "bottom" of the stack; all additions to the stack are made through
    the "top". One implementation of a stack is the undo command in an
    application. The most recent action (the current web page, recently
    typed word, etc.) is found at the top of the action history. To access
    previous actions, you move in the reverse order that the actions were made
    (most recent to oldest).

    This stack implementation uses a Python list, with the "top" of the stack
    defined as the right side of the list and the "bottom" of the stack as the
    left side. This definition allows the stack to take advantage of the O(1)
    performance of list appends and pops for adding and removing entries to the
    stack.
    """
    def __init__(self):
        """Constructor, initializes an empty stack."""
        self.items = []

    def is_empty(self):
        """Returns True if instance there are no items are on the stack."""
        return self.items == []

    def peek(self):
        """Returns the last item in the stack."""
        return self.items[-1]

    def push(self, item):
        """
        Adds item to the top of the stack.

        Variable
        --------
        item
            Object to add to the top of the stack.
        """
        self.items.append(item)

    def pop(self):
        """Returns and removes the last item on the stack."""
        return self.items.pop()

    def size(self):
        """Returns the height of the stack."""
        return len(self.items)


if __name__ == "__main__":
    s = Stack()
