#!/usr/bin/env python3
"""
A simple command line calculator.
"""
import re
import time

from stacks import infix_to_postfix, compute_postfix


def main():

    print("To quit, press 'q'.")

    time.sleep(.5)
    while True:
        expression = input("Calculate: ")
        if expression == "q":
            break

        # Clean input so that there is at least one space between operands and
        # operators.
        # Add a space between an operator and a parentheses.
        expression = re.sub(r"(\*\*|[\*\^+-/])([()])", r"\1 \2", expression)
        expression = re.sub(r"([()])(\*\*|[\*\^+-/])", r"\1 \2", expression)
        # Add space between digits and operators.
        expression = re.sub(r"""(?<=\d|[ ])       # Look behind for a digit or
                                                  # a space
                                (\*\*|[\*\^+-/])  # Match the exponent operator
                                                  # **, or any of the other
                                                  # operators; multiplication
                                                  # (*), division (/), addition
                                                  # (+), subtraction (-), or
                                                  # exponent (^).
                                (?=\d|[ ]|$)      # Look ahead for a digit or
                                                  # a space.
                            """,
                            r" \1 ",
                            expression,
                            flags=re.VERBOSE)
        # Add a space between digits and open parenthesis.
        expression = re.sub(r"""(\()(\d+)  # Matches an open parenthesis
                                           # followed by one or more digits.
                            """,
                            r"\1 \2",
                            expression,
                            flags=re.VERBOSE)
        # Add a space between digits and close parenthesis.
        expression = re.sub(r"""(\d+)(\))  # Matches an one or more digits
                                           # followed by a close
                                           #  parenthesis.
                            """,
                            r"\1 \2",
                            expression,
                            flags=re.VERBOSE)
        postfix_expression = infix_to_postfix(expression)
        print(compute_postfix(postfix_expression))


if __name__ == "__main__":
    main()
