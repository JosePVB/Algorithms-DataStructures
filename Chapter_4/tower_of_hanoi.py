#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Functions to solve the tower of Hanoi problem.
"""
def move_disk(from_pole, to_pole):
    """
    Move the disk from `from_pole` to `to_pole`.
    """
    print("Moving disk from {} to {}".format(from_pole, to_pole))

def move_tower(height, from_pole, to_pole, with_pole):
    """
    Prints the steps required to solve a tower of Hanoi problem of height
    `height`.

    Parameters
    ----------
    height : int
        Number of disks on the tower.
    from_pole : object
        Object that represents the first pole. Tower begins on this pole.
    to_pole : object
        Object that represent the final pole. Tower will end on this pole.
    with_pole : object
        Object that represents the third pole. This is the assistant pole.
    """
    if height >= 1:
        move_tower(height - 1, from_pole, with_pole, to_pole)
        move_disk(from_pole, to_pole)
        move_tower(height - 1, with_pole, to_pole, from_pole)

if __name__ == "__main__":
    move_tower(4, 0, 1, 2)

