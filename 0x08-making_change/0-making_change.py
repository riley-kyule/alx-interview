#!/usr/bin/python3
"""
Coin change problem

"""
from typing import List


def makeChange(coins: List[int], total: int) -> int:
    """
    Return fewest number of coins needed to meet `total`
    Returns `-1` if `total` cannot be met by any number of coins available
    """
    if total <= 0:
        return 0
    d_soln = [total + 1] * (total + 1)
    d_soln[0] = 0

    for n in range(1, total + 1):
        for coin in coins:
            if n - coin >= 0:
                d_soln[n] = min(d_soln[n], 1 + d_soln[n - coin])
    return d_soln[total] if d_soln[total] != total + 1 else - 1