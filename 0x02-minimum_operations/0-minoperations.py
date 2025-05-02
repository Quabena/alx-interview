#!/usr/bin/python3
"""
Module for calculating minimum number of operations to get n H characters.
"""


def minOperations(n):
    """
    Determines the minimal number of operations to generate n 'H' characters
    using only copy and paste operations.
    """
    if not isinstance(n, int) or n < 2:
        return 0

    total_ops = 0
    current = 1
    buffer = 0

    while current < n:
        if buffer == 0:
            # First copy and paste to initialize
            buffer = current
            current += buffer
            total_ops += 2
        elif (n - current) % current == 0:
            # Copy and paste when the remaining characters can be built evenly
            buffer = current
            current += buffer
            total_ops += 2
        else:
            # Just paste from the buffer
            current += buffer
            total_ops += 1

    return total_ops
