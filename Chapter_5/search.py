#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Searching algorithms.
"""
import itertools

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