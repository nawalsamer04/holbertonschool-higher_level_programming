#!/usr/bin/python3
"""
Module that multiplies two matrices using NumPy
"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
    Multiply two matrices using NumPy
    """
    try:
        return (np.matmul(m_a, m_b)).tolist()
    except Exception as e:
        raise e
