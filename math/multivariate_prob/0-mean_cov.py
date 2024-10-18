#!/usr/bin/env python3
import numpy as np


def mean_cov(X):
    """
    Calculate the mean and covariance matrix of a dataset.

    Parameters:
    X (numpy.ndarray): A 2D array of shape (n, d) containing the dataset,
                       where n is the number of data points and d is the
                       number of dimensions.

    Returns:
    tuple: A tuple containing:
        - mean (numpy.ndarray): An array of shape (1, d) containing the mean
          of the dataset.
        - cov (numpy.ndarray): An array of shape (d, d) containing the
          covariance matrix of the dataset.

    Raises:
    TypeError: If X is not a 2D numpy.ndarray.
    ValueError: If X contains less than 2 data points.

    Note:
    This function does not use numpy.cov to calculate the covariance matrix.
    """
    if not isinstance(X, np.ndarray) or X.ndim != 2:
        raise TypeError("X must be a 2D numpy.ndarray")

    n, d = X.shape
    if n < 2:
        raise ValueError("X must contain multiple data points")

    # Calculate mean
    mean = np.mean(X, axis=0, keepdims=True)

    # Calculate covariance
    X_centered = X - mean
    cov = np.dot(X_centered.T, X_centered) / (n - 1)

    return mean, cov
  