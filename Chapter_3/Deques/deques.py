#!/usr/bin/env python3


class Deque:
    """
    Implementation of a deque (double-ended queue) abstract data type. Items
    can be added and removed from either side of the deque.

    This implmentation has O(1) appends and pops from the right side and
    O(n) appends and pops from the left side.
    """
    def __init__(self, items=None):
        if items is None:
            self.items = []
        else:
            if isinstance(items, list):
                self.items = items
            else:
                try:
                    self.items = [item for item in items]
                except TypeError:
                    raise

    def __len__(self):
        return len(self.items)

    def append_right(self, item):
        """Append item to the right end of the deque."""
        self.items.append(item)

    def append_left(self, item):
        """Insert item on the left side of the deque."""
        self.items.insert(0, item)

    def pop_right(self):
        """Returns the item on the right end of the deque."""
        return self.items.pop()

    def pop_left(self):
        """Returns the item on the left end of the deque."""
        return self.items.pop(0)

    def __getitem__(self, position):
        return self.items[position]

    def __add__(self, other):
        """Append all items of other unto the right side of the deque."""
        try:
            for item in other:
                self.append_right(item)
        except TypeError:
            # other is not iterable
            raise
        return Deque(items=self.items)

    def __radd__(self, other):
        """Append all items of other unto the left side of the deque."""
        try:
            for item in reversed(other):
                self.append_left(item)
        except TypeError:
            # other is not iterable
            raise
        return Deque(items=self.items)

    def __repr__(self):
        return "Deque({})".format(repr(self.items))

    def __str__(self):
        return repr(self)

    def __bool__(self):
        return bool(self.items)

    def __mul__(self, n):
        return Deque(self.items * n)

    def __pow__(self, n):
        """Every element in the deque is repeated n times."""
        return Deque((repeat_item
                      for item in self.items
                      for repeat_item in [item] * n))

    def __eq__(self, other):
        try:
            return self.items == other.items
        except AttributeError:
            return False
