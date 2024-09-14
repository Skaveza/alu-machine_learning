#!/usr/bin/env python3
"""
Module that performs element-wise addition,subtraction, multiplication and division
"""


def np_elementwise(mat1, mat2):
    """Performs element-wise addition, subtraction, multiplication, and division.
    
    Args:
        mat1: A numpy array.
        mat2: A numpy array or scalar value.

    Returns:
        A tuple containing the element-wise sum, difference, product, and quotient (in that order).
    """
    return (mat1 + mat2, mat1 - mat2, mat1 * mat2, mat1 / mat2)
