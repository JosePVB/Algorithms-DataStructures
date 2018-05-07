#!/usr/bin/env python3
"""
A simulation of a hot potato game using a Queue.
"""
from queues import Queue


def hot_potato(names, num):
    """
    Simulate a game of hot potato.

    The person in the front of the queue is moved to the back of the Queue.
    This is repeated num times, at which point the person in the front of the
    Queue is permanently removed. This process is repeated until only one
    person remains.

    Variables
    ---------
    names, list or tuple
        The list of people that will play hot potato.
    num, int
        The number of times the potato will switch hands before the unfortunate
        bearer is removed.
    """
    hot_potato_queue = Queue()

    # Add the names to the hot potato Queue.
    for name in names:
        hot_potato_queue.enqueue(name)

    # Let the fun begin!
    while hot_potato_queue.size() > 1:
        for pass_the_potato in range(num):
            hot_potato_queue.enqueue(hot_potato_queue.dequeue())
        # Sorry, you have the hot potato. Better luck next time!
        hot_potato_queue.dequeue()

    # And the winner is...
    print("And the winner is {}!".format(hot_potato_queue.dequeue()))


if __name__ == "__main__":
    import random

    names = [
        "Lil' Jimmy",
        "John from marketing",
        "Santa",
        "Uncle Al",
        "a mini pig"
    ]
    random.shuffle(names)
    hot_potato(names, num=3)
