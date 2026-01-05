#!/usr/bin/python3
"""101-lazy_matrix_mul module"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiply two matrices using NumPy"""
    try:
        return np.matmul(m_a, m_b)
    except ValueError:
        raise ValueError("m_a and m_b can't be multiplied")
    except TypeError:
        raise TypeError("Scalar operands are not allowed, use '*' instead")

