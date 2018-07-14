#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module to convert one string into another. The allowed actions, and their
respective costs are:
    - Copy one letter from one one to anothr: 5
    - Insert a letter:                        20
    - Delete a letter:                        20

Applied method is recursive.
"""
from functools import lru_cache

@lru_cache()
def string_edit(str1, str2):

    if len(str1) == 0:
        return 20 * len(str2)

    if len(str2) == 0:
        return 20 * len(str1)

    if str1[-1] == str2[-1]:
        return string_edit(str1[:-1], str2[:-1])
    else:
        min_steps = min(
            5 + string_edit(str1[:-1], str2[:-1]),  # Replace character
            20 + string_edit(str1, str2[:-1]),  # Insert character
            20 + string_edit(str1[:-1], str2)  # Delete character
        )
    return min_steps

if __name__ == "__main__":
    print(string_edit('hello', 'hop'))
