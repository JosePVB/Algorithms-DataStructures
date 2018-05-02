#!/usr/bin/env python3
"""
Script tests the performance of list and dictionary operations for inputs
of different magnitudes.
"""


def list_concat():
    """Creates a list by looping and concatenation."""
    l = []
    for num in range(1000):
        l = l + [num]


def list_append():
    """Creates a list by appending."""
    l = []
    for num in range(1000):
        l.append(num)


def list_comprehension():
    """Creates a list using string comprehension."""
    l = [num for num in range(1000)]


def list_cast():
    """Creates a list through casting."""
    l = list(range(1000))


if __name__ == "__main__":

    import timeit
    import random

    timer_list_concat = timeit.Timer('list_concat()',
                                     'from __main__ import list_concat')
    timer_list_append = timeit.Timer('list_append()',
                                     'from __main__ import list_append')
    timer_list_comprehension = timeit.Timer('list_comprehension()',
                                            'from __main__ '
                                            'import list_comprehension')
    timer_list_cast = timeit.Timer('list_cast()',
                                   'from __main__ import list_cast')
    print("\nTesting performance of different list creation methods.")
    print("concat: ", timer_list_concat.timeit(number=1000), " milliseconds.")
    print("append: ", timer_list_append.timeit(number=1000), " milliseconds.")
    print("comprehension: ",
          timer_list_comprehension.timeit(number=1000),
          " milliseconds.")
    print("cast: ", timer_list_cast.timeit(number=1000), " milliseconds.")

    # Test performance between popping at the end of a list vs at index 0 for
    # lists of different sizes.

    timer_popzero = timeit.Timer('x.pop(0)', 'from __main__ import x')
    timer_pop = timeit.Timer('x.pop()', 'from __main__ import x')

    print("\n\nTesting performance between popping "
          "at first and last index.")
    for exp in range(3, 7):
        num = 10**exp
        x = list(range(num))
        print("Pop at [0] for {:,} elements: ".format(num),
              timer_popzero.timeit(number=1000),
              " milliseconds.")
        x = list(range(num))
        print("Pop at [-1] for {:,} elements: ".format(num),
              timer_pop.timeit(number=1000),
              " milliseconds.")

    # Test performance of the contains operator for lists and dictionaries.

    print('\n\nTesting contains performance of lists and dictionaries.')
    for exp in range(3, 7):
        num = 10**exp
        # Test list.
        x = list(range(num))
        timer = timeit.Timer('random.randrange({}) in x'.format(num),
                             'from __main__ import random, x')
        print("List of {:,} elements: ".format(num),
              timer.timeit(number=1000),
              " milliseconds.")
        # Test dictionary
        x = {i: None for i in range(num)}
        print("Dict of {:,} elements: ".format(num),
              timer.timeit(number=1000),
              " milliseconds.")

    # Test performance of the list index operation
    print("\n\nTesting the list index operation.")
    for exp in range(3, 7):
        num = 10**exp
        x = list(range(num))
        timer = timeit.Timer('x[random.randrange({})]'.format(num),
                             'from __main__ import random, x')
        print("List index for {0:,} elements: ".format(num),
              timer.timeit(number=1000),
              " milliseconds.")

    # Test the performance of the get and set for dictionaries.
    print('\n\nTesting the performance of get item and set item'
          ' for dicitonaries.')
    for exp in range(3, 7):
        num = 10**exp
        x = {i: None for i in range(num)}
        set_timer = timeit.Timer('x[random.randrange({})] = None'.format(num),
                                 'from __main__ import random, x')
        get_timer = timeit.Timer('x.get(random.randrange({}))'.format(num),
                                 'from __main__ import random, x')
        print("Set for {:,} elements: ".format(num),
              set_timer.timeit(number=1000),
              " milliseconds.")
        print("Get for {:,} elements: ".format(num),
              get_timer.timeit(number=1000),
              " milliseconds.")
