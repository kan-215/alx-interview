#!/usr/bin/python3
"""
Change-making problem solution.
"""


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet the total amount.
    
    Args:
        coins (list): A list of coin denominations.
        total (int): The target total amount.
    
    Returns:
        int: The fewest number of coins needed to make the total,
             or -1 if the total cannot be made.
    """
    if total <= 0:
        return 0

    # Sort the coins in descending order
    coins = sorted(coins, reverse=True)
    count = 0

    for coin in coins:
        if total == 0:
            break
        # Use as many of the current coin as possible
        count += total // coin
        total %= coin

    # If total is not 0 it means we can't make the total with the given coins
    return count if total == 0 else -1
