#!/usr/bin/env python3


def linear_kth_smallest(iterable, k):
    """
    Task: Given a list of numbers in random order, write a linear time
    algorithm to find the kth smallest integer in the list.

    Assumptions: iterable is read only.

    Final algorithm is linear in time -- O(kn), as list indexing and appending
    is O(1) and the iterable of length n is looped over k times.

    Variables
    ---------
    iterable, list or tuple
        Iterable of random integers.
    k, int
    """
    # Initialize list that will contain the smallest integers.
    list_of_mins = []

    # Loop over the iterable k times.
    for _ in range(k):
        min_int = None
        for num in iterable:
            if min_int is None:
                min_int = num
            else:
                # Set min_int equal to current num if current num is less than
                # min_int.
                if len(list_of_mins) == 0:
                    if num < min_int:
                        min_int = num
                else:
                    # If list_of_mins is not empty, current num must
                    # also be greater than the last entry into list_of_mins.
                    if num < min_int and num > list_of_mins[-1]:
                        min_int = num
        list_of_mins.append(min_int)
    return list_of_mins[-1]


def nlogn_kth_smallest(iterable, k):
    """
    Task: Improve the linear time algorithm to be O(nlogn).

    Assumptions: iterable is read only and every value is unique.

    Final algorithm is, on average, O(nlogn) as this is equivalent to the
    average performance of the sorted() function; indexing is O(1).
    """
    return sorted(iterable)[k-1]


if __name__ == "__main__":
    import random

    k = 3
    random_ints = [random.randint(0, 100) for _ in range(20)]
    print(random_ints, '\n', linear_kth_smallest(random_ints, k))
    print(nlogn_kth_smallest(random_ints, k))
