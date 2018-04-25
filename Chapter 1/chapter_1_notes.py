#!/usr/bin/env python3

"""
This script contains the examples developed throughout the chapter 1
of the 'Problem Solving with Algorithms and Data Structures using Python'
"""

# Fraction class

def gcd(m, n):
    """Returns the greatest common denominator between m and n.

    Variables
    ---------
    m, int
    n, int
    """
    # Euclid's Algorithm
    while m % n != 0:
        previous_m = m
        previous_n = n

        m = previous_n
        n = previous_m % previous_n
    return n


class Fraction():
    """Class implements the abstract data type of Fraction."""
    def __init__(self, numerator, denominator):
        """Constructor.

        Variables
        ---------
        numerator, int
        dnoominator, int
        """
        self.numerator = numerator
        self.denominator = denominator

    def __str__(self):
        """Overwrites defafult __str__() to visually look like a fraction."""
        return "{}/{}".format(self.numerator, self.denominator)

    def __add__(self, other_fraction):
        """Overwrites the default __add__() for fraction addition.

        General fraction addition:  a/b + c/d = (d*a + c*b) / (b*d)
        Variables
        ---------
        other_fraction, Fraction
        """
        new_numerator = (self.numerator * other_fraction.denominator
                         + self.denominator * other_fraction.numerator)
        new_denominator = self.denominator * other_fraction.denominator
        greatest_common_denominator = gcd(new_numerator, new_denominator)
        return Fraction(new_numerator // greatest_common_denominator,
                        new_denominator // greatest_common_denominator)


if __name__ == "__main__":
    print(Fraction(3, 5))
    print(Fraction(2, 5) + Fraction(1, 5))
