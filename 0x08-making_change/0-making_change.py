#!/usr/bin/python3
"""
This module contains a function to determine
the fewest number of coins needed to meet a given amount.
"""


def makeChange(coins, total):
    """
    Calculates the fewest number of coins needed to meet total

    Args:
        coins (list): List of the values of coins available
        total (int): The target amount

    Returns:
        int: Fewest number of coins needed to meet total
             or -1 if not possible
    """
    if total <= 0:
        return 0

    # Initialize DP table with a high value (total + 1 is the "infinity")
    dp = [total + 1] * (total + 1)
    dp[0] = 0  # Base case: 0 coins to make 0

    for amt in range(1, total + 1):
        for coin in coins:
            if coin <= amt:
                dp[amt] = min(dp[amt], dp[amt - coin] + 1)

    return dp[total] if dp[total] != total + 1 else -1
