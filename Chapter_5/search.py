#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Searching algorithms.
"""

def sequential_search(item, iterable):
	"""
	Search if `item` is in `iterable`.

	Returns
	-------
	bool
		True if `item` is in `iterable.
	"""
	return any(item == i for i in iterable)

def binary_search(item, values):
	"""
	Search if `item` is in `values`.

	Parameters
	----------
	item : object
	values : list

	Returns
	-------
	bool
		True if `item` is in `values`.
	"""
	# Check if the list is empty; return False.
	if not values:
		return False

	# Find the middle of the list.
	middle = len(values) // 2
	middle_value = values[middle]

	# Check if the value at the middle index is the item of interest;
	# return True
	if middle_value == item:
		return True

	# Check if the item is greater than the middle item; recurse with
	# list of items after the middle index.
	if item > middle_value:
		return binary_search(item, values[middle+1:])
	# Otherwise, recurse with the list of items before the middle index.
	return binary_search(item, values[:middle])


class Map:
	"""
	Implementation of the Map abstract data type.

	The class uses the simple remainder method to calculate the hash values.
	"""

	def __init__(self):
		# Number of elements held by the instance within its has table.
		# Value is arbritary but should be a prime number to ensure
		# an optimal collision resolution algorithm.
		self.size = 11

		# Will hold the keys.
		self.slots = [None for _ in range(self.size)]

		# Will hold the values for each key.
		self.data = [None for _ in range(self.size)]

	def hashfunction(self, key):
		"""
		Compute the hash of the key.

		Parameters
		----------
		key : int

		Returns
		-------
		int
		"""
		return key % self.size

	def rehash(self, old_hash):
		"""
		Calculate the new hash value, using a `plus one` method.

		Parameters
		----------
		old_hash : int

		Returns
		-------
		int
		"""
		return (old_hash + 1) % self.size

	def put(self, key, value):
		"""
		Store the key and value within the instance.

		If `key` is already stored, the value will be updated to the
		provided `value`.
		"""
		index = self.hashfunction(key)

		# Check if the value at the index is None; store the values.
		if self.slots[index] is None:
			self.slots[index] = key
			self.data[index] = value

		# Check if the value at the index is the same as `key`; update the
		# value.
		elif self.slots[index] == key:
			self.data[index] = value
		else:
			# Hash collision.
			new_index = self.rehash(index)

			# Deal with additional hash collisions.
			while (self.slots[new_index] is not None
					and self.slots[new_index] != key):
				new_index = self.rehash(new_index)
			if self.slots[new_index] is None:
				self.slots[new_index] = key
				self.data[new_index] = value
			else:
				self.data[new_index] = value

	def get(self, key, value=None):
		"""
		Get the value associated with `key`.

		Can provide additional positional parameter, whose value will be
		returned if `key` is not stored by the instance.
		"""
		starting_index = self.hashfunction(key)

		stop = False  # True if all hash values have been searched.
		current_index = starting_index

		while not stop:
			if self.slots[current_index] is None:
				return value
			elif self.slots[current_index] == key:
				return self.data[current_index]
			else:
				current_index = self.rehash(current_index)
				if current_index == starting_index:
					stop = True

		return value

	def __setitem__(self, key, value):
		self.put(key, value)

	def __getitem__(self, key):
		value = self.get(key)
		if value is None:
			raise KeyError('{}'.format(repr(key)))
		return value
