#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
A maze solver.
"""
import turtle

PART_OF_PATH = 'O'
TRIED = '.'
OBSTACLE = '+'
DEAD_END = '-'

def search_from(maze, initial_row, initial_column):
    """
    Recursive algorithm to find the exit of a maze.

    The algorithm will recursively try to go to the north. If this does not
    succeed, it will try to go south, followed by west and east.

    Parameters
    ----------
    maze : Maze
        The Maze object that the algorithm needs to solve.
    initial_row : int
        Row index of the current position.
    initial_column : int
        COlumn index of the current position.
    """
    maze.update_position(initial_row, initial_column)
    # Check the first three base cases.
    # 1. Run into an obstacle; return False.
    if maze[initial_row][initial_column] == OBSTACLE:
        return False
    # 2. Found a square that has already been explored; return False.
    if maze[initial_row][initial_column] == TRIED:
        return False
    # 3. Found an outside edge not occupied by an obstacle; the exit.
    if maze.is_exit(initial_row, initial_column):
        maze.update_position(initial_row, initial_column, PART_OF_PATH)
        return True

    maze.update_position(initial_row, initial_column, TRIED)

    # Try each direction: North, South, West, East.
    found = (
        search_from(maze, initial_row - 1, initial_column)
        or search_from(maze, initial_row + 1, initial_column)
        or search_from(maze, initial_row, initial_column - 1)
        or search_from(maze, initial_row, initial_column + 1)
    )

    if found:
        maze.update_position(initial_row, initial_column, PART_OF_PATH)
    else:
        maze.update_position(initial_row, initial_column, DEAD_END)
    return found

class Maze:

    def __init__(self, maze_file_name):
        """
        Builds an internal representation of the maze and finds the starting
        position of the turtle.

        Parameters
        ----------
        maze_file_name : str
            Path to the text file that contains the maze. Walls should be
            represented by '+' and maze routes by a space, ' '.
        """
        self.maze_list = []

        with open(maze_file_name, 'r') as maze_file:
            rows = 0
            for line in maze_file:
                row_list= []
                cols = 0
                for char in line[:-1]:  # -1 to exclude new line character
                    row_list.append(char)
                    if char == 'S':
                        self.start_row = rows
                        self.start_col = cols
                    cols += 1
                rows += 1
                self.maze_list.append(row_list)

        self.rows_in_maze = rows
        self.columns_in_maze = cols
        self.x_translate = -cols / 2
        self.y_translate = rows / 2

        self.turtle = turtle.Turtle(shape='turtle')
        self.window = turtle.Screen()
        self.window.setworldcoordinates(
            -(cols - 1) / 2 - 0.5,
            -(rows - 1) / 2 - 0.5,
            (cols - 1) / 2 + 0.5,
            (rows - 1) / 2 + 0.5
        )

    def __getitem__(self, position):
        return self.maze_list[position]

    def draw_centered_box(self, x, y, color):
        """
        Draws a box centered around (`x`,`y`).

        Parameters
        ----------
        x : int
            x coordinate
        y : int
            y coordinate
        color : str
            Color of the inside of the box.
        """
        turtle.tracer(0)
        self.turtle.up()
        self.turtle.goto(x - 0.5, y - 0.5)
        self.turtle.color('black', color)
        self.turtle.setheading(90)
        self.turtle.down()
        self.turtle.begin_fill()
        for i in range(4):
            self.turtle.forward(1)
            self.turtle.right(90)
        self.turtle.end_fill()
        turtle.update()
        turtle.tracer(1)

    def draw_maze(self):
        """Draws the boundaries of the maze."""
        for y in range(self.rows_in_maze):
            for x in range(self.columns_in_maze):
                if self[y][x] == OBSTACLE:
                    self.draw_centered_box(
                        x + self.x_translate,
                        -y + self.y_translate,
                        'tan'
                    )
        self.turtle.color('black', 'blue')

    def move_turtle(self, x, y):
        """Moves the turtle to the specified position."""
        self.turtle.up()
        self.turtle.setheading(
            self.turtle.towards(x + self.x_translate, -y + self.y_translate)
        )
        self.turtle.goto(x + self.x_translate, -y + self.y_translate)

    def drop_bread_crumb(self, color):
        """
        Visually indicate the path taken by the turtle.

        Parameters
        ----------
        color : str
            Color of the dot.
        """
        self.turtle.dot(color)

    def update_position(self, row, col, value=None):
        """
        Moves the turtle and drops a breadcrumb.

        Parameters
        ----------
        row : int
            Row index to go to.
        col : int
            Column index to go to.
        value : str, default = None
            Single length character to assign to the internal representation
            of the maze.
        """
        if value is not None:
            self[row][col] = value

        self.move_turtle(col, row)

        if value == PART_OF_PATH:
            color = "green"
        elif value == OBSTACLE:
            color = "red"
        elif value == TRIED:
            color = "black"
        elif value == DEAD_END:
            color = "red"
        else:
            color = None

        if color is not None:
            self.drop_bread_crumb(color)

    def is_exit(self, row, col):
        """
        Checks whether the position is an exit.

        Parameters
        ----------
        row : int
            Row index of position.
        col : int
            Column index of the position
        """
        return (
            row == 0
            or row == self.rows_in_maze - 1
            or col == 0
            or col == self.columns_in_maze - 1
        )


if __name__ == "__main__":
    MAZE_FILE = ('maze2.txt')
    my_maze = Maze(MAZE_FILE)
    my_maze.draw_maze()
    search_from(my_maze, my_maze.start_row, my_maze.start_col)
    my_maze.window.exitonclick()

