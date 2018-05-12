#!/usr/bin/env python3
"""
Implements a function that returns True if the word or phrase is a palindrome.
"""
import re

import Chapter_3.Deques.deques as deques


def palchecker(string):
    """
    Function returns True if the string is a palindrome.

    Variables
    ---------
    string, str
    """
    # Remove whitespace characters.
    deque = deques.Deque(re.sub(r'\s', '', string))

    while deque.pop_left() == deque.pop_right() and len(deque) > 1:
        continue

    return 0 <= len(deque) <= 1
