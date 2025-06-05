#!/usr/bin/python3
"""
Module 0-rotate_2d_matrix
This module contains a function that rotates a 2D matrix 90
degrees clockwise.
The operation is done in-place with no return.
"""


def rotate_2d_matrix(matrix):
    """
    Rotates a square 2D matrix 90 degrees clockwise in-place.

    Args:
        matrix (list of lists): The n x n 2D matrix to be rotated.

    Returns:
        None
    """
    n = len(matrix)

    # Transpose the matrix (swap rows with columns)
    for i in range(n):
        for j in range(i + 1, n):
            # Swap elements across the diagonal
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse each row to complete the rotation
    for row in matrix:
        row.reverse()
