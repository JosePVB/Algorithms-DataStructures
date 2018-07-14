#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Functions to draw a Sierpinski triangle.
"""
import turtle

def get_midpoint(first_point, second_point):
    """
    Returns the midpoint given two vector-like subscriptable objects.

    Parameters
    ----------
    first_point : int or float subscriptable object
    second_point : int or float subscriptable object
    """
    return (
        (first_point[0] + second_point[0]) / 2,
        (first_point[1] + second_point[1]) / 2
    )

def draw_triangle(points, color, my_turtle):
    """
    Draws a filled triangle.

    Parameters
    ----------
    points : list of tuples or subscriptable object
        A list of 3 x, y points that represent the coordinates of the
        triangle's lower left, top, and lower right points.
    color : str
       The fill color of the triangle.
    my_turtle : turtle.Turtle
        A class instance of turtle.Turtle.
    """
    my_turtle.penup()
    my_turtle.goto(points[0])
    my_turtle.pendown()

    my_turtle.fillcolor(color)
    my_turtle.begin_fill()
    my_turtle.goto(points[1])
    my_turtle.goto(points[2])
    my_turtle.goto(points[0])
    my_turtle.end_fill()

def sierpinski(points, degree, my_turtle):
    """
    Draws a Sierpinski triangle.

    Parameters
    ----------
    points : list of tuples or subscriptable object
        A list of 3 x, y points that represent the coordinates of the
        triangle's lower left, top, and lower right points.
    degree : int
        The degree of the fractal; the number of times to divide the main
        triangle.
    my_turtle : turtle.Turtle
        A class instance of turtle.Turtle.
    """
    colormap = [
        'blue',
        'red',
        'green',
        'white',
        'yellow',
        'violet',
        'orange'
    ]
    draw_triangle(points, colormap[degree], my_turtle)
    if degree > 0:
        sierpinski(
            [points[0],
             get_midpoint(points[0], points[1]),
             get_midpoint(points[0], points[2])],
            degree - 1,
            my_turtle
        )
        sierpinski(
            [points[1],
             get_midpoint(points[1], points[2]),
             get_midpoint(points[1], points[0])],
            degree - 1,
            my_turtle
        )
        sierpinski(
            [points[2],
             get_midpoint(points[2], points[0]),
             get_midpoint(points[2], points[1])],
            degree - 1,
            my_turtle
        )


if __name__ == "__main__":
    my_turtle = turtle.Turtle()
    my_window = my_turtle.getscreen()
    my_window.setup(height=1500, width=1500)
    points = [(-200, -100), (0, 200), (200, -100)]
    sierpinski(points, 5, my_turtle)
    my_window.exitonclick()

