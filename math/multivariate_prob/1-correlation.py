#!/usr/bin/env python3
import numpy as np


def correlation(C):
    """
    Calculate the correlation matrix from a covariance matrix.

    Parameters:
    C (numpy.ndarray): A 2D square array of shape (d, d) containing
                       a covariance matrix.

    Returns:
    numpy.ndarray: An array of shape (d, d) containing the correlation matrix.

    Raises:
    TypeError: If C is not a numpy.ndarray.
    ValueError: If C is not a 2D square matrix.
    """
    if not isinstance(C, np.ndarray):
        raise TypeError("C must be a numpy.ndarray")

    if C.ndim != 2 or C.shape[0] != C.shape[1]:
        raise ValueError("C must be a 2D square matrix")

    """Calculate the standard deviations"""
    std_devs = np.sqrt(np.diag(C))

    """Calculate the correlation matrix"""
    correlation_matrix = C / np.outer(std_devs, std_devs)

    return correlation_matrix
