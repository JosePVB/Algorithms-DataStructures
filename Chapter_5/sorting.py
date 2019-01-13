#!/usr/bin/env python3
#! -*- coding: utf-8 -*-
"""
Sorting algorithms.
"""

def bubble_sort(values):
    """
    Implementation of the bubble sort algorithm.

    Parameters
    ----------
    values : list

    Returns
    -------
    Sorted list

    Example
    -------
    >>> bubble_sort([4,2,3,1])
    [1,2,3,4]
    >>> bubble_sort([1,2,3,4])
    [1,2,3,4]
    """
    swapped = True  # Flag to indicate if a pair of values was swapped.
    iteration = len(values) - 1

    while iteration > 0 and swapped:
        swapped = False  # Assume that all values are sorted at this iteration.
        
        for i in range(iteration):
            if values[i] > values[i + 1]:
                swapped = True
                values[i], values[i + 1] = values[i + 1], values[i]

        iteration -= 1
    return values

def selection_sort(values):
    """
    Implementation of the selection sort algorithm.

    Parameters
    ----------
    values : list

    Returns
    -------
    Sorted list
    """
    iterations = len(values) - 1
    # Make n - 1 passes through the list.
    for iteration in range(iterations, 0, -1):
        index_of_max = iteration
        for i in range(iteration):
            if values[i] > values[index_of_max]:
                index_of_max = i
        values[iteration], values[index_of_max] = (
            values[index_of_max], values[iteration]
        )
    return values

def insertion_sort(values, starting_index=0, gap=1):
    """
    Implementation of the insertion sort algorithm.

    Parameters
    ----------
    values : list
        Values to sort
    starting_index : int, default = 0
        The index at which to begin sorting.
    gap : int, default = 1
        Sort items that are this number apart. By default, sorts all contiguous
        items (the entire list).

    Returns
    -------
    Sorted list
    """
    if not values:
        return values
    if starting_index < 0:
        raise IndexError('`starting_index` must be a positive index')
    # Need to loop over the list. Assume that the value at the starting index
    # is already in order.
    for i in range(starting_index+gap, len(values), gap):
        current_value = values[i]
        # Need variable to track position at index of sublist.
        position = i

        # Sequentially search sublist for the index at which the
        # `current_value should be inserted. If the current value in the
        # sublist is greater than `current_value`, increase the index of the
        # value in the sublist.
        while position > 0 and values[position-gap] > current_value:
            values[position]  = values[position-gap]
            position -= gap
        values[position] = current_value
    return values

def shell_sort(values):
    """
    Implementation of the selection sort algorithm.

    Parameters
    ----------
    values : list

    Returns
    -------
    Sorted list
    """

    # Sort `gap` sublists.
    number_of_sublists = len(values) // 2
    while number_of_sublists > 0:

        for i in range(number_of_sublists):
            values = insertion_sort(
                values,
                starting_index=i,
                gap=number_of_sublists
            )
        
        number_of_sublists //= 2

    return values

def merge_sort(values, **kwargs):
    """
    Implementation of the merge sort algorithm.

    Parameters
    ----------
    values : list
        Values to sort
    
    Returns
    -------
    A sorted list
    """
    start_index = kwargs.get('_start_index', 0)
    end_index = kwargs.get('_end_index', len(values))
    number_of_values = end_index - start_index
    result = [0] * number_of_values
    if number_of_values <= 1:
        if result:
            result[0] = values[start_index]
        return result
    
    middle = number_of_values // 2 + start_index
    left_list = merge_sort(values, _start_index=start_index, _end_index=middle)
    right_list = merge_sort(
        values,
        _start_index=middle,
        _end_index=end_index
    )
    # Merge the sorted items.
    length_of_left_list = len(left_list)
    length_of_right_list = len(right_list)
    left_index = 0  # Current position in the `left_list`.
    right_index = 0  # Current position in the `right_list`.
    result_index = 0  # Current position in the `result` list.

    # Compare the elements in the left list to the right list. Pick the
    # smallest value and add it to the `result` list.
    while (
            left_index < length_of_left_list
            and right_index < length_of_right_list):
        left_value = left_list[left_index]
        right_value = right_list[right_index]
        if left_value < right_value:
            result[result_index] = left_value
            left_index += 1
        else:
            result[result_index] = right_value
            right_index += 1
        result_index += 1
    
    # Add the remaining elements in the left list. Elements within a list
    # are sorted.
    while left_index < length_of_left_list:
        result[result_index] = left_list[left_index]
        left_index += 1
        result_index += 1
    
    # Add the remaining elements in the right list. Elements within a list
    # are sorted.
    while right_index < length_of_right_list:
        result[result_index] = right_list[right_index]
        right_index += 1
        result_index += 1
    
    return result


        
    
    
