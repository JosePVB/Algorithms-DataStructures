#!/usr/bin/env python3
"""
Module implements a simple stack data structure.
"""
import operator


class Stack:
    """
    The stack data type follows a Last In First Out (LIFO) ordering. This means
    that newer items are near the "top" of the stack, while older items are
    near the "bottom" of the stack; all additions to the stack are made through
    the "top". One implementation of a stack is the undo command in an
    application. The most recent action (the current web page, recently
    typed word, etc.) is found at the top of the action history. To access
    previous actions, you move in the reverse order that the actions were made
    (most recent to oldest).

    This stack implementation uses a Python list, with the "top" of the stack
    defined as the right side of the list and the "bottom" of the stack as the
    left side. This definition allows the stack to take advantage of the O(1)
    performance of list appends and pops for adding and removing entries to the
    stack.
    """
    def __init__(self):
        """Constructor, initializes an empty stack."""
        self.items = []

    def is_empty(self):
        """Returns True if instance there are no items are on the stack."""
        return self.items == []

    def peek(self):
        """Returns the last item in the stack."""
        return self.items[-1]

    def push(self, item):
        """
        Adds item to the top of the stack.

        Variable
        --------
        item
            Object to add to the top of the stack.
        """
        self.items.append(item)

    def pop(self):
        """Returns and removes the last item on the stack."""
        return self.items.pop()

    def size(self):
        """Returns the height of the stack."""
        return len(self.items)


def balanced_parentheses(string, open_chars='({[<'):
    """
    Returns True if string contains a balanced number of parentheses; the
    number of open parentheses equals the number of close parentheses.

    Returns False if the number of parentheses are not equal.

    The algorithm reads the string from left to right and adds an open
    character to the Stack on every open character. The most recent entry into
    the Stack is removed on every corresponding closed character.

    Variables
    ---------
    string, str
        String containing any one of the character that need to be balanced.
    open_chars, iterable; default = '({[<'
        Iterable containing the characters that need to be balanced, such as
        '(', '{', '[', and/or '<'.
    """
    stack = Stack()

    # Construct closing characters.
    def f(x): return ')' if x == '(' else chr(ord(x)+2)
    close_chars = ''.join(map(f, open_chars))

    # Parse string left to right
    for char in string:
        # Check for open character
        if char in open_chars:
            stack.push(char)
        elif char in close_chars:
            try:
                if (close_chars.index(char)
                        == open_chars.index(stack.peek())):
                    stack.pop()
                else:
                    # Open and close character do not do not correspond.
                    return False
            except IndexError:
                # There are no more open characters.
                return False

    return stack.is_empty()


def base_converter(base_ten_int, base=2):
    """
    Converts the integer to the number system with a user defined base.

    Assumes that integer is greater than 0.

    Variables
    ---------
    base_ten_int, int
        Integer to convert; assumed to be greater than 0.
    base, int; default = 2
        Number system base, between 2 and 16, with which the integer will be
        converted.
    """
    if base_ten_int <= 0:
        raise ValueError("Need to provide aN integer greater than 0.")

    if not 2 <= base <= 16:
        raise ValueError("Base must be between 2 and 16.")

    digits = "0123456789ABCDEF"
    stack = Stack()

    while base_ten_int > 0:
        # Add remainder to the stack.
        stack.push(base_ten_int % base)
        base_ten_int = base_ten_int // base

    return ''.join(digits[stack.pop()] for _ in range(stack.size()))


def infix_to_postfix(infix_expression):
    """
    Returns the postfix version of the expression.

    Infix expressions have the operator in between the operands, while postfix
    expressions have the operators after the operands, reading left to right.

    Example (IMS - Intermediate Step):

    Infix:      ( A + B ) * ( C - E ) ^ D - F
        IMS 1:  ( A B + ) * ( C E - ) ^ D - F
        IMS 2:  ( A B + ) * ( C E - D ^ ) - F
        IMS 3:  ( A B + C E - D ^ * ) - F
    Postfix:    A B + C E - D ^ * F -

    Variables
    ---------
    infix_expression, string
        Space delimited infix expression composed of multiplication (*),
        division (/), addition (+), subtraction (-), exponential (^ or **),
        and/or parentheses characters.
    """
    # Set up
    operator_stack = Stack()  # Will keep track of operators in the expression.
    postfix = []  # Will contain the postfix expression.

    # Define operator precedence.
    operator_precedence = {
        "(": 0,  # Given the lowest precedence such that any other operator
                 # will go above it.
        ")": 0,
        "^": 3,
        "**": 3,
        "*": 2,
        "/": 2,
        "+": 1,
        "-": 1
    }

    # Loop over the expression.
    for char in infix_expression.upper().split():
        if char in operator_precedence:
            if char == "(":
                operator_stack.push(char)
            elif char == ")":
                # Append all operators to the postfix expression up until the
                # corresponding open parenthesis.
                while (not operator_stack.is_empty()
                        and operator_stack.peek() != "("):
                        postfix.append(operator_stack.pop())
                if not operator_stack.is_empty():
                    operator_stack.pop()  # Remove open parenthesis.
            else:
                char_precedence = operator_precedence[char]
                # Append any operators of greater or equal precendence already
                # on the Stack to the postfix expression; add operator to the
                # Stack.
                while (not operator_stack.is_empty()
                        and (char_precedence
                             <= operator_precedence[operator_stack.peek()])):
                        postfix.append(operator_stack.pop())
                operator_stack.push(char)
        else:
            postfix.append(char)

    # Finished looping over the expression; append any remaining operators on
    # the stack to the postfix list.
    while not operator_stack.is_empty():
        postfix.append(operator_stack.pop())
    return " ".join(postfix)


def compute_postfix(postfix_expression):
    """
    Returns the computed postfix expression.

    Variables
    ---------
    postfix_expression, str
        Space delimited postfix expression containing integers and
        exponential (^ or **), multiplication (*), division (/), addition (+),
        and/or subtraction (-) symbols.
    """
    # Setup
    operand_stack = Stack()
    operations = {
        "^": operator.__pow__,
        "**": operator.__pow__,
        "*": operator.__mul__,
        "/": operator.__truediv__,
        "+": operator.__add__,
        "-": operator.__sub__
    }

    # Loop over the expression.
    for char in postfix_expression.split():
        try:
            operand_stack.push(int(char))
        except ValueError:
            # char is an operator; compute the operation using the two most
            # recent entries in the operand_stack.
            try:
                second_operand, first_operand = (
                    operand_stack.pop() for _ in range(2)
                )
            except IndexError:
                raise ValueError("Need two operands before the "
                                 "'{}' operator.".format(char))
            # Add computation back unto the operand_stack for further
            # computations.
            operand_stack.push(operations[char](first_operand, second_operand))

    # Remaining entry in the operand_stack is the final result.
    return operand_stack.pop()


if __name__ == "__main__":
    s = Stack()
    print(balanced_parentheses('(())'))
    print(base_converter(233453))
    print(infix_to_postfix("( 15 + 6 ) * ( C - E ) ^ D - F"))
    print(compute_postfix("7 8 + 8 2 + /"))
