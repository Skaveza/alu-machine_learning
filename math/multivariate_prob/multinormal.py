#!/usr/bin/env python3
"""
Module for MultiNormal class representing a Multivariate Normal distribution.
"""

import numpy as np


class MultiNormal:
    """
    Represents a Multivariate Normal distribution.
    """

    def __init__(self, data):
        """
        Initialize the MultiNormal distribution.

        Parameters:
        data (numpy.ndarray): A 2D array of shape (d,n) containing the dataset,
                              where d is the number of dimensions and
                              n is the number of data points.

        Raises:
        TypeError: If data is not a 2D numpy.ndarray.
        ValueError: If data contains less than 2 data points.
        """
        if not isinstance(data, np.ndarray) or data.ndim != 2:
            raise TypeError("data must be a 2D numpy.ndarray")

        d, n = data.shape
        if n < 2:
            raise ValueError("data must contain multiple data points")

        # Calculate mean
        self.mean = np.mean(data, axis=1, keepdims=True)

        # Calculate covariance
        centered_data = data - self.mean
        self.cov = np.dot(centered_data, centered_data.T) / (n - 1)

    def pdf(self, x):
        """
        Calculate the Probability Density Function (PDF) at a data point.

        Parameters:
        x (numpy.ndarray): A 2D array of shape (d,1) containing the data point,
                           where d is the number of dimensions.

        Returns:
        float: The value of the PDF at the given point.

        Raises:
        TypeError: If x is not a numpy.ndarray.
        ValueError: If x does not have the shape (d, 1).
        """
        d, _ = self.mean.shape

        if not isinstance(x, np.ndarray):
            raise TypeError("x must be a numpy.ndarray")

        if x.shape != (d, 1):
            raise ValueError("x must have the shape ({}, 1)".format(d))

        # Compute the PDF
        det = np.linalg.det(self.cov)
        inv_cov = np.linalg.inv(self.cov)
        diff = x - self.mean
        exponent = -0.5 * np.dot(np.dot(diff.T, inv_cov), diff)
        coefficient = 1 / np.sqrt((2 * np.pi) ** d * det)

        return float(coefficient * np.exp(exponent))
