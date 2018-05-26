#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Example of recursion to draw a spiral.
"""
from turtle import Turtle

def draw_spiral(my_turtle, line_length):
    if line_length > 0:
        my_turtle.forward(line_length)
        my_turtle.right(90)
        draw_spiral(my_turtle, line_length - 5)


if __name__ == "__main__":
    # Instantiate the turtle and window
    my_turtle = Turtle()
    my_window = my_turtle.getscreen()

    # Draw the spiral
    draw_spiral(my_turtle, 100)

    # Close the window
    my_window.exitonclick()

