#!/usr/bin/python3
"""
Module 0-island_perimeter
This module defines a function that calculates the perimeter
of an island in a 2D grid representation.
"""


def island_perimeter(grid):
    """
    Calculates the perimeter of the island described in grid.

    Args:
        grid (list of list of int): 2D grid representing the map
            where 0 = water and 1 = land.

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                perimeter += 4
                if i > 0 and grid[i - 1][j] == 1:
                    perimeter -= 1
                if i < len(grid) - 1 and grid[i + 1][j] == 1:
                    perimeter -= 1
                if j > 0 and grid[i][j - 1] == 1:
                    perimeter -= 1
                if j < len(grid[i]) - 1 and grid[i][j + 1] == 1:
                    perimeter -= 1
    return perimeter
