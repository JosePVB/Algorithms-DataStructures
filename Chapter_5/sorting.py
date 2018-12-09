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
