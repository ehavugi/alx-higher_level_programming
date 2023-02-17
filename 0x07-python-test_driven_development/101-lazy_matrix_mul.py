#!/usr/bin/python3
"""
    lazy matrix multiplier using numpy
"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """
        Lazy_matrix_mul multiplies m_a and m_b using numpy

    """
    a = np.array(m_a)
    b = np.array(m_b)
    c = np.matmul(a, b)
    return c
