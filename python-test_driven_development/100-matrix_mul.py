#!/usr/bin/python3
"""
Module that multiplies 2 matrices.
"""


def matrix_mul(m_a, m_b):
    """Multiply two matrices.

    Args:
        m_a: first matrix (list of lists of int/float)
        m_b: second matrix (list of lists of int/float)

    Returns:
        New matrix = m_a * m_b
    """
    # ---- Validate m_a ----
    if type(m_a) is not list:
        raise TypeError("m_a must be a list")
    if len(m_a) == 0:
        raise ValueError("m_a can't be empty")
    if any(type(row) is not list for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if m_a == [[]] or any(len(row) == 0 for row in m_a):
        raise ValueError("m_a can't be empty")
    if any(type(x) not in (int, float) for row in m_a for x in row):
        raise TypeError("m_a should contain only integers or floats")
    row_len_a = len(m_a[0])
    if any(len(row) != row_len_a for row in m_a):
        raise TypeError("each row of m_a must be of the same size")

    # ---- Validate m_b ----
    if type(m_b) is not list:
        raise TypeError("m_b must be a list")
    if len(m_b) == 0:
        raise ValueError("m_b can't be empty")
    if any(type(row) is not list for row in m_b):
        raise TypeError("m_b must be a list of lists")
    if m_b == [[]] or any(len(row) == 0 for row in m_b):
        raise ValueError("m_b can't be empty")
    if any(type(x) not in (int, float) for row in m_b for x in row):
        raise TypeError("m_b should contain only integers or floats")
    row_len_b = len(m_b[0])
    if any(len(row) != row_len_b for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    # ---- Validate multiplication compatibility ----
    if row_len_a != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # ---- Multiply ----
    result = []
    for i in range(len(m_a)):
        new_row = []
        for j in range(len(m_b[0])):
            s = 0
            for k in range(len(m_b)):
                s += m_a[i][k] * m_b[k][j]
            new_row.append(s)
        result.append(new_row)

    return result
