#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import turtle

def fractal_tree(my_turtle, branch_length):
    """
    Draw a fractal tree.

    Parameters
    ----------
    my_turtle : turtle.Turtle
        Instance used to draw the fractal tree.
    branch_length : int
        Length of the branch to draw.
    """
    if branch_length > 5:
        my_turtle.forward(branch_length)
        my_turtle.right(20)
        fractal_tree(my_turtle, branch_length - 15)
        my_turtle.left(40)
        fractal_tree(my_turtle, branch_length - 15)
        my_turtle.right(20)
        my_turtle.backward(branch_length)


if __name__ == "__main__":
    my_turtle = turtle.Turtle()
    my_window = my_turtle.getscreen()
    my_turtle.left(90)
    my_turtle.up()
    my_turtle.backward(300)
    my_turtle.down()
    my_turtle.color('green')
    fractal_tree(my_turtle, 110)
    my_window.exitonclick()

