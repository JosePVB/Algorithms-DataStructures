#!/usr/bin/env python3
"""
Implementation of an unordered list by constructing a linked list.

The location of the first item of the list must be explicitly specified; often
referred to as the HEAD of the list. Once we know where the first item is,
this item can tell us where the second item is and so on.
"""


class Node:
    """
    The basic building block for the linked list. Each instance must hold two
    pieces of information; the list item itself and a reference to the next
    Node in the list.
    """
    def __init__(self, item):
        self.item = item
        self.next_node = None  # Denotes that there is no next Node.

    def __repr__(self):
        return "Node({})".format(repr(self.item))

    def __str__(self):
        return repr(self)

    def __next__(self):
        return self.next_node

    def get_item(self):
        return self.item

    def set_item(self, item):
        self.item = item

    def set_next_node(self, next_node):
        self.next_node = next_node


class UnorderedList:
    """
    The list contains a reference to the first Node; the other Nodes in the
    list are linked to the following Nodes by explicit references.
    """
    def __init__(self):
        """
        Contructor creates an empty list.

        The head of the list refers to the first node that contains the first
        item of the list.

        The class does not contain any node objects, but only a single
        reference to the first node in the linked structure.
        """
        self.head = None

    def add(self, item):
        """
        Adds a node to the list that contains item.

        As an unordered list, the relative position of items is not important,
        therefore new nodes will be added to the beginning of the list.

        Parameters
        ---------
        item : object
            Object to store within the linked list.
        """
        # Create a new Node object.
        new_node = Node(item)
        # Attach the existing list to the new Node.
        new_node.set_next_node(self.head)
        # The head of the list will now reference this new Node.
        self.head = new_node

    def __bool__(self):
        """Return True if the head of the list is not None."""
        return self.head is not None

    def __iter__(self):
        """Support for iteration."""
        current_node = self.head
        while current_node is not None:
            yield current_node
            current_node = next(current_node)

    def __len__(self):
        """ Returns the length of the list."""
        return sum(1 for node in self)

    def __contains__(self, item):
        """
        Returns True if the list contains the item.

        Parameters
        ---------
        item : object
            Object to search for in the list.
        """
        for node in self:
            if node.get_item() == item:
                return True
        return False

    def __eq__(self, other):
        """Compares two linked lists."""
        self_items = [node.get_item() for node in self]
        other_items = [node.get_item() for node in other]
        return self_items == other_items

    def __getitem__(self, position):
        """
        Return the item held by the Node at the provided position.

        If a slice is passed, a linked list is returned that contains
        the Nodes at these positions.

        Parameters
        ---------
        position : integer or slice
        """
        current_length = len(self)

        # Check if value is a slice.
        if not isinstance(position, slice):
            # Raise error is position is greater than length of list.
            if current_length + position < 0 or position >= current_length:
                raise IndexError("list index out of range")
            # Modify position if negative.
            position = current_length + position if position < 0 else position
            for num, node in enumerate(self):
                if num == position:
                    return node.get_item()
        else:
            # Obtain the start and stop indeces from the slice.
            start, stop = (
                current_length + index  # Negative index
                if index is not None and index < 0
                else index if index is not None  # Positive index
                else 0 if num == 0  # No start index ([:num])
                else current_length  # No stop index ([num:])
                for num, index in enumerate((position.start, position.stop))
            )
            # Raise ValueError for a step value of 0
            if position.step == 0:
                raise ValueError("slice step cannot be zero")
            step = 1 if position.step is None else position.step

            ul = UnorderedList()  # Will be returned

            # Check if slice is valid.
            if ((start > stop and step < 0)
                or (start < stop and step > 0)
                or (start == 0 and stop == current_length)):
                # The class implementation follows a LIFO ordering. The first
                # item added to the list is at the last index. To return a new
                # linked list with the proper ordering, the items must be
                # accessed in the reverse order they were added.
                node_list = [
                    node for num, node in enumerate(self)
                    if (((start <= num < stop) or (start >= num > stop))
                        and (num - start) % step == 0)
                ]
                for node in reversed(node_list) if step > 0 else node_list:
                    ul.add(node.get_item())
            return ul

    @staticmethod
    def _repr_format(nodes, string):
        return string.join(str(node) for node in nodes)

    def __repr__(self):
        format_string = "UnorderedList({nodes})"
        arrow = "->"
        if not self:
            return format_string.format(nodes="")
        else:
            if len(self) > 7:
                first_three_nodes = UnorderedList._repr_format(self[:3], arrow)
                last_three_nodes = UnorderedList._repr_format(self[-3:], arrow)
                nodes = (
                    first_three_nodes
                    + "...".join([arrow]*2)
                    + last_three_nodes
                )
            else:
                nodes = UnorderedList._repr_format(self, arrow)
            return format_string.format(nodes=nodes)

    def remove(self, item):
        """
        Removes the first instance of item from the linked list.

        Parameters
        ---------
        item : object
            Object to remove from the list.
        """
        previous_node = None
        current_node = self.head
        found = False

        while current_node is not None and not found:
            if current_node.get_item() == item:
                found = True
            else:
                previous_node = current_node
                current_node = next(current_node)

        if found:
            if previous_node is None:
                self.head = next(current_node)
            else:
                previous_node.set_next_node(next(current_node.get_next_node))
        else:
            raise ValueError("{} not in list.".format(repr(item)))

    def append(self, item):
        """
        Appends `item` to the end of the linked list.

        Parameters
        ----------
        item : object
            Object to add to the end of the unordered linked list.
        """
        if not self:
            self.head = Node(item)
        else:
            # Loop until the last Node currently in the list.
            last_index = len(self) - 1
            for num, node in enumerate(self):
                if num == last_index:
                    node.set_next_node(Node(item))

    def index(self, item):
        """
        Returns the index of the first ocurrance of `item` in the list.

        Parameters
        ----------
        item : object
            The object that will be searched for in the list.

        Returns
        -------
        index : int
            The position of `item` within the linked list.

        Raises
        ------
        ValueError
            If `item` is not within the list.
        """
        for index, node in enumerate(self):
            if item == node.get_item():
                return index
        raise ValueError("{} is not in list".format(repr(item)))

    def pop(self):
        """
        Removes the last Node in the linked list and returns its item.

        Returns
        -------
        object
            Item held within the last Node of the linked list.

        Raises
        ------
        IndexError
            If list is empty.
        """
        if self:
           if len(self) == 1:
                item = self.head.get_item()
                self.head = None
                return item
           for num, node in enumerate(self):
                if num == len(self) - 2:
                    item = next(node).get_item()
                    node.set_next_node(None)
                    return item
        raise IndexError("pop from empty list")

    def insert(self, position, item):
        """
        Add the item at the given position.

        `item` is added at the beginning or at the end of the list if
        the magnitude of `position` is greater than the length of the list.

        Parameters
        ----------
        position : int
            Index at which to insert `item`
        item : object
            Object to insert into the linked list.
        """
        current_length = len(self)
        position = (
            current_length - 1
            if position >= current_length > 1
            else 1 if position >= current_length == 1
            else 0 if position <= -current_length
            else current_length + position if position < 0
            else position
        )
        if not self or position == 0:
            self.add(item)
        else:
            for num, node in enumerate(self):
                if num == position - 1:
                    new_node = Node(item)
                    next_node = next(node)
                    if next_node is not None:
                        new_node.set_next_node(next_node)
                    node.set_next_node(new_node)


if __name__ == "__main__":
    ul = UnorderedList()
    for i in range(5):
        ul.add(i)
