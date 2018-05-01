#!/usr/bin/env python3
"""Script tests the performance of list and dictionary operations."""


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
    """
    Here is the final output.

    Testing performance of different list creation methods.


    concat:  3.0565415769815445  milliseconds
    append:  0.17854132698266767  milliseconds
    comprehension:  0.07684464097837918  milliseconds
    cast:  0.03300053800921887  milliseconds


    Testing performance between popping at first and last index.


    Pop at [0] for 1,000 elements:  0.0005668539961334318  milliseconds
    Pop at [-1] for 1,000 elements:  0.0002143520105164498  milliseconds
    Pop at [0] for 10,000 elements:  0.006415733019821346  milliseconds
    Pop at [-1] for 10,000 elements:  0.00021288497373461723  milliseconds
    Pop at [0] for 100,000 elements:  0.06899165798677132  milliseconds
    Pop at [-1] for 100,000 elements:  0.000239285989664495  milliseconds
    Pop at [0] for 1,000,000 elements:  1.3821034340071492  milliseconds
    Pop at [-1] for 1,000,000 elements:  0.00022224400890991092  milliseconds
    Pop at [0] for 10,000,000 elements:  15.198659743997268  milliseconds
    Pop at [-1] for 10,000,000 elements:  0.00022028799867257476  milliseconds


    Testing contains performance of lists and dictionaries.


    List of 1,000 elements:  0.016853645007358864  milliseconds.
    Dict of 1,000 elements:  0.002178505004849285  milliseconds.
    List of 10,000 elements:  0.15340963000198826  milliseconds.
    Dict of 10,000 elements:  0.0023701569880358875  milliseconds.
    List of 100,000 elements:  1.519411809014855  milliseconds.
    Dict of 100,000 elements:  0.0032649300119373947  milliseconds.
    List of 1,000,000 elements:  15.116391540010227  milliseconds.
    Dict of 1,000,000 elements:  0.002498740010196343  milliseconds.
    List of 10,000,000 elements:  148.0063763129874  milliseconds.
    Dict of 10,000,000 elements:  0.0032509609882254153  milliseconds.

    """
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
