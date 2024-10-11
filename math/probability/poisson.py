#!/usr/bin/env python3
"""This module illustrates Poisson Distribution."""


class Poisson:
    """Represents a Poisson Distribution."""

    def __init__(self, data=None, lambtha=1.):
        """
        Initialize the Poisson distribution.

        Parameters:
        data: A list of data points to estimate the distribution.
        lambtha: The expected number of occurrences in a given time frame.

        If data is provided, lambtha is calculated as the mean of the data.
        Otherwise, the provided lambtha is used.

        Raises:
        TypeError: If data is not a list.
        ValueError: If lambtha is not positive or if data has fewer 
        than two data points.
        """
        if lambtha <= 0:
            raise ValueError("lambtha must be a positive value")

        if data is None:
            self.lambtha = float(lambtha)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.lambtha = float(sum(data) / len(data))
