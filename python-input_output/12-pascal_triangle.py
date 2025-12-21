#!/usr/bin/python3
"""
Module that defines a function to generate Pascal's Triangle.
"""


def pascal_triangle(n):
    """
    Returns a list of lists of integers representing
    Pascal’s triangle of size n.

    Args:
        n (int): Number of rows of Pascal's triangle

    Returns:
        list: A list of lists of integers
    """
    if n <= 0:
        return []

    triangle = []

    for i in range(n):
        row = [1]

        if triangle:
            last_row = triangle[-1]
            for j in range(1, len(last_row)):
                row.append(last_row[j - 1] + last_row[j])
            row.append(1)

        triangle.append(row)

    return triangle
