#!/usr/bin/env python3
"""This module illustrates Poison Distribution"""

class Poisson:
  """Represents Poisson Distribution"""
  def __init__(self, data=None, lambtha=1.):
        # Check if lambtha is a positive value
        if lambtha <= 0:
            raise ValueError("lambtha must be a positive value")

        # If data is provided, calculate lambtha from the data
        if data is None:
            # Use the provided lambtha if no data is given
            self.lambtha = float(lambtha)
        else:
            # Validate the data type
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            # Check if data has at least two data points
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            # Calculate lambtha as the mean of the data
            self.lambtha = float(sum(data) / len(data))
