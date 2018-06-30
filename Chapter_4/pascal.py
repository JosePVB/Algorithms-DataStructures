#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Pascal triangle class.
"""
from Chapter_4.recursive_exercises import factorial

def binomial_coefficient(n, r):
    """
    Compute the binomial coeffient.
    """
    return factorial(n) // (factorial(r) * factorial(n-r))

class PascalTriangle:

    def __init__(self, nrows):
        self.nrows = nrows
        self.num_coefficients = sum(range(self.nrows + 1))

    def _gen_row(self, n):
        """
        Generate the numbers in the nth row.

        Parameters
        ----------
        n : int
            0 indexed row.

        Returns
        -------
        generator
        """
        return (binomial_coefficient(n, i) for i in range(n + 1))

    def __getitem__(self, n):
        """
        Returns the numbers at row `n`.

        Parameters
        ----------
        n : int
            0 indexed row.

        Returns
        -------
        tuple

        Raises
        ------
        IndexError
            Speciied row is larger than the number of rows in the triangle.
        """
        if n >= self.nrows:
            msg = "row index out of range"
            raise IndexError(msg)
        return tuple(self._gen_row(n))

    def __str__(self):

        format_rows =  (
            "    ".join(str(num) for num in self._gen_row(row))
            for row in range(self.nrows)
        )
        return "\n".join(row.center(5*(self.nrows - 1) + self.nrows) for row in format_rows)

if __name__ == "__main__":
    p = PascalTriangle(10)
    print(p)

