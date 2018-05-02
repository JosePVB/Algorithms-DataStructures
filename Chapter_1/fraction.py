#!/usr/bin/env python3

"""
Implements a Fraction class that behaves like a fraction. This includes
basic mathematical operations as well as boolean comparators. Unary negation
and inversion (reciprocal) are also included.
"""


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
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError('Both the numerator and denominator must be ints.')

        if denominator < 0:
            numerator = -numerator
            denominator = abs(denominator)

        greatest_common_denominator = abs(gcd(numerator, denominator))
        self.numerator = numerator // greatest_common_denominator
        self.denominator = denominator // greatest_common_denominator

    def __str__(self):
        """Overwrites defafult __str__() to visually look like a fraction."""
        if self.denominator == 1:
            return str(self.numerator)
        return "{}/{}".format(self.numerator, self.denominator)

    def __add__(self, other_fraction):
        """Implements fraction addition.

        General fraction addition:  a/b + c/d = (d*a + c*b) / (b*d)

        Variables
        ---------
        other_fraction, Fraction
        """
        new_numerator = (self.numerator * other_fraction.denominator
                         + self.denominator * other_fraction.numerator)
        new_denominator = self.denominator * other_fraction.denominator
        return Fraction(new_numerator, new_denominator)

    def __eq__(self, other_fraction):
        """Implements fraction equality.

        Variables
        ---------
        other_fraction, Fraction
        """
        first_numerator = self.numerator * other_fraction.denominator
        second_numerator = self.denominator * other_fraction.numerator
        return first_numerator == second_numerator

    def __sub__(self, other_fraction):
        """Implements fraction subtraction.

        General fraction subtraction: a/b - c/d = (a * d - c * b) / (b * d)

        Variables
        ---------
        other_fraction, Fraction
        """
        new_numerator = (self.numerator * other_fraction.denominator
                         - self.denominator * other_fraction.numerator)
        new_denominator = self.denominator * other_fraction.denominator
        return Fraction(new_numerator, new_denominator)

    def __mul__(self, other_fraction):
        """Implements fraction multiplication.

        General fraction multiplication: a/b * c/d = (a * c) / (b * d)

        Variables
        ---------
        other_fraction, Fraction
        """
        new_numerator = self.numerator * other_fraction.numerator
        new_denominator = self.denominator * other_fraction.denominator
        return Fraction(new_numerator, new_denominator)

    def __truediv__(self, other_fraction):
        """Implements fraction division.

        General fraction division: a/b / c/d = (a * d) / (b * c)

        Variables
        ---------
        other_fraction, Fraction
        """
        new_numerator = self.numerator * other_fraction.denominator
        new_denominator = self.denominator * other_fraction.numerator
        return Fraction(new_numerator, new_denominator)

    def __le__(self, other_fraction):
        """Implements less than or equal to for fractions.

        General equation: a/b <= c/d -> a*d <= b*c

        Variables
        ---------
        other_fraction, Fraction
        """
        lhs = self.numerator * other_fraction.denominator
        rhs = self.denominator * other_fraction.numerator
        return lhs <= rhs

    def __lt__(self, other_fraction):
        """Implements less than for fractions.

        General equation a/b < c/d -> a*d < b*c

        Variables
        ---------
        other_fraction, Fraction
        """
        lhs = self.numerator * other_fraction.denominator
        rhs = self.denominator * other_fraction.numerator
        return lhs < rhs

    def __ge__(self, other_fraction):
        """Implements greater than or equal to for fractions.

        General equation a/b >= c/d -> a*d >= b*c

        Variables
        ---------
        other_fraction, Fraction
        """
        lhs = self.numerator * other_fraction.denominator
        rhs = self.denominator * other_fraction.numerator
        return lhs >= rhs

    def __gt__(self, other_fraction):
        """Implements greater than for fractions.

        General equation a/b > c/d -> a*d > b*c

        Variables
        ---------
        other_fraction, Fraction
        """
        lhs = self.numerator * other_fraction.denominator
        rhs = self.denominator * other_fraction.numerator
        return lhs > rhs

    def __ne__(self, other_fraction):
        """Implements fraction inequality.

        Variables
        ---------
        other_fraction, Fraction
        """
        first_numerator = self.numerator * other_fraction.denominator
        second_numerator = self.denominator * other_fraction.numerator
        return first_numerator != second_numerator

    def __neg__(self):
        """Implements unary negation."""
        return Fraction(-self.numerator, self.denominator)

    def __pos__(self):
        return self

    def __invert__(self):
        """Implements unary inversion, i.e. the reciprocal."""
        return Fraction(self.denominator, self.numerator)
