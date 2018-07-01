#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Module to solve the following problem:
    There are two unmarked jugs of size m and of size n.
    There is a pump that can be used to fill the jugs with water.
    Describe the steps to have d units of water in a jug.
"""
import re


from Chapter_1.fraction import gcd

DIGITS = re.compile(r'\d+')

class WaterJug:
    """
    Water jugs with empty and fill methods.

    Parameters
    ----------
    volume : int
        Volume of water that the water jug can hold.
    """
    def __init__(self, volume):
        self.volume = volume
        self._contents = []

    @property
    def isfull(self):
        return len(self._contents) == self.volume

    @property
    def isempty(self):
        return not bool(self._contents)


    @property
    def content(self):
        return len(self._contents)

    def empty(self, into=None):
        """
        Empty the contents of the water jug.

        If `into` is not None, the contents of the water jug are poured into
        `into`. Otherwise, the entire content of the water jug is emptied.

        Parameters
        ----------
        into : WaterJug, default = None
            Water jug to fill.
        """
        if into is None:
            print("Emptying contents of {}".format(self))
            self._contents = []
        else:
            print("Emptying contents of {0} into {1}".format(self, into))
            while not into.isfull and not self.isempty:
                into.fill(self)

    def fill(self, _from=None):
        """
        Fill the water jug.
        """
        if _from is None:
            print("Filling {}".format(self))
            self._contents = [1] * self.volume
        else:
            self._contents.append(_from._contents.pop())

    def __repr__(self):
        return "WaterJug({})".format(self.volume)

    def __str__(self):
        return repr(self)

def fill_jugs(small_jug, big_jug, desired_volume):
    """
    Fill the one of the unmarked jugs with `desired_volume` of water.

    Parameters
    ----------
    small_jug : WaterJug

    big_jug : WaterJug

    desired_volume : int
        Desired volume of water.
    """
    jug_contents = (small_jug.content, big_jug.content)

    # Check if contents of either jug is equal to the desired volume.
    if any(desired_volume == content for content in jug_contents):
        jug = small_jug if small_jug.content == desired_volume else big_jug
        msg = "The current content of {jug} is {volume}"
        print(msg.format(jug=jug, volume=desired_volume))
    else:
        if big_jug.isfull:
            big_jug.empty()
        small_jug.fill()
        small_jug.empty(into=big_jug)
        fill_jugs(small_jug, big_jug, desired_volume)

def main():
    input_str = input(
        "Provide the size of the first and second water jugs and"
        " what the desired volume is: "
    )
    try:
        volume_jug_1, volume_jug_2, desired_volume = (
            int(digit) for digit in DIGITS.findall(input_str)[:3]
        )
    except ValueError:
        print("\nPlease provide 3 distinct digits.\n")
        main()
    else:
        if volume_jug_1 == volume_jug_2:
            msg = "Jugs must be of different volumes"

        if desired_volume % gcd(volume_jug_1, volume_jug_2) != 0:
            msg = (
                "Greatest common factor between the water jug volumes"
                " must be a factor of the desired volume."
            )

        if 'msg' in locals():
            print(msg)
            retry = input("Would you like to retry? (y/n):")
            if retry.lower() == "y":
                main()
        else:
            small_jug, big_jug = (
                WaterJug(volume)
                for volume in sorted((volume_jug_1, volume_jug_2))
            )

            # Switch the alias of the water jugs if the desired volume
            # is the difference between the big and small jugs.
            # This prevents RecursionError from being raised.
            if (desired_volume == big_jug.volume - small_jug.volume
                and (big_jug.volume - small_jug.volume) % 2 == 0):
                small_jug, big_jug = big_jug, small_jug

            fill_jugs(small_jug, big_jug, desired_volume)


if __name__ == "__main__":
    main()

