#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from functools import lru_cache

def minimum_coins_v1(coins, change, known_change):
    """
    Given a list of coins, return the minimum number of coins needed for the
    change.

    Parameters
    ----------
    coins, list-like
        List of coin values to use.

    change, float
        The value that the coins need to add up to.

    known_change, dict
        Dictionary with change/minimum number of coins key/value pairs.

    Returns
    -------
    int
        The number of coins to make change.
    """
    # Check base case; change in coins or known change.
    if change in coins or change in known_change:
        try:
            return known_change[change]
        except KeyError:
            known_change[change] = 1
        return 1

    min_coins = change

    # Change can only be composed of coins whose value is less than or equal
    # to the remaining change.
    valid_coins = tuple(coin for coin in coins if coin <= change)

    for coin in valid_coins:
        num_coins = (
            1 + minimum_coins_v1(valid_coins, change - coin, known_change)
        )
        if num_coins < min_coins:
            min_coins = num_coins
            known_change[change] = min_coins
    return min_coins


@lru_cache()
def minimum_coins_v2(coins, change):
    """
    Simplified version of the previous minimum_coins function using the
    lru_cache() decorator.

    Given a list of coins, return the minimum number of coins needed for the
    change.

    Parameters
    ----------
    coins, list-like
        List of coin values to use.

    change, float
        The value that the coins need to add up to.

    Returns
    -------
    int
        The number of coins to make change.
    """
    min_coins = change

    # Check the base case.
    if change in coins:
        return 1

    valid_coins = tuple(coin for coin in coins if coin <= change)

    for coin in valid_coins:
        num_coins = 1 + minimum_coins(valid_coins, change - coin)
        if num_coins < min_coins:
            min_coins = num_coins
    return min_coins


if __name__ == "__main__":
    print(minimum_coins_v1((1,5,10,21,25), 63, dict()))
    print(minimum_coins_v2((1,5,10,21,25), 63))

