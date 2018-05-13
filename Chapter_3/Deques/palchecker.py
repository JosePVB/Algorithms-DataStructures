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

    # Flag to identify if characters match.
    chars_match = True

    # Consume the elements in the Deque at both ends until the length
    # of the Deque is less than or equal to one.
    while chars_match and len(deque) > 1:
        left_char = deque.pop_left()
        right_char = deque.pop_right()

        if left_char != right_char:
            chars_match = False

    return chars_match
