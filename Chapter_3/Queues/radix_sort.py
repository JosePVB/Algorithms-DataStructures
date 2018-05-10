#!/usr/bin/env python3
"""
Implementation of a radix sort machine.
"""
from Chapter_3.Queues import queues


def radix_sort(iterable, reverse=False):
    """
    Returns a sorted list of integers.

    The radix sort uses a collection of bins; a main bin and a bin, for base 10
    numbers, for each of the 10 digits, 0-9.

    The function loops over every place value for each number and places them
    in the corresponding digits bin. Once all the numbers have been placed in a
    bin, the digits bin are emptied into the main bin, from 0 to 9.
    This process then repeats for the following place value.

    The bins act like queues.

    Variables
    ---------
    iterable, list or tuple
        Iterable containing integers.
    reverse, bool; default = False
        If False, returns the iterable sorted from smallest to largest, else
        the numbers are sorted largest to smallest. The behavior is the same
        as the built in sorted() function.
    """
    # Setup

    # Create bins.
    bins = {"main": queues.Queue()}
    bins.update({i: queues.Queue() for i in range(10)})

    # Place all numbers in the "main" bin; convert numbers to string for
    # indexing.
    for num in iterable:
        bins["main"].enqueue(num)

    # Find character length of maximum number; this will define until what
    # place value the function needs to loop.
    max_place_index = len(str(max(bins["main"].items)))

    # Sort; loop over every place value.
    for place_index in range(max_place_index):
        # Empty the "main" bin and place into corresponding digit bins.
        while not bins["main"].is_empty():
            current_number = bins["main"].dequeue()
            bin_for_current_number = (current_number // 10 ** place_index) % 10
            bins[bin_for_current_number].enqueue(current_number)
        # Add numbers back into the "main" bin.
        for i in range(9, -1, -1) if not reverse else range(10):
            current_digit_bin = bins[i]
            while not current_digit_bin.is_empty():
                bins["main"].enqueue(current_digit_bin.dequeue())
    return bins["main"].items
