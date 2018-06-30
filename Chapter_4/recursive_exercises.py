#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Recursive exercises.
"""

def factorial(n):
    """
    Compute the factorial of `n`.

    Parameters
    ----------
    n : int

    Returns
    -------
    int

    Raises
    ------
    ValueError
        When `n` is less than 0.
    """
    if n < 0:
        msg = "Provided value must be greater than or equal to 0."
        raise ValueError(msg)

    if n <= 1:
        return 1

    return n * factorial(n-1)

def reverse_list(iterable):
    """
    Reverse the contents of an iterable.

    Parameters
    ----------
    iterable

    Returns
    -------
    list
    """
    copy = list(iterable)
    if len(copy) == 1:
        return copy
    return [copy[-1]] + reverse_list(copy[:-1])

if __name__ == "__main__":
    print(reverse_list(num for num in range(11)))
