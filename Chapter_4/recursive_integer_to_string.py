#!/usr/bin/env python3


def int_to_str(n, base):
    """
    Converts an integer to a string in a base between binary and hexadecimal.

    Parameters
    ----------
    n : int
        Integer to convert to a string.
    base : int
        Integer, between 2 and 16, that specifies the base of the string
        representation.

    Returns
    -------
    str
        The representation of `n` in the specified base.

    Raises
    ------
    ValueError
        The provided `base` does not fall between 2 and 16.
    """
    if base < 2 or base > 16:
        raise ValueError(("base needs to be between "
                          "binary and hexadecimal, [2, 16]"))

    integer_chars = "0123456789ABCDEF"

    if n < base:
        return integer_chars[n]
    else:
        quotient, remainder = divmod(n, base)
        return int_to_str(quotient, base) + integer_chars[remainder]

