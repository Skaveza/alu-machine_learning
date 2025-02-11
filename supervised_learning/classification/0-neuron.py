#!/usr/bin/env python3
"""This module defines a single Neuoron performing binary classification"""


import numpy as np


class Neuron:
    """Defines a single neuron performing binary classification"""

    def __init__(self, nx):
        """
        Initializes the neuron.

        Parameters:
        nx (int): Number of input features.

        Raises:
        TypeError: If nx is not an integer.
        ValueError: If nx is less than 1.
        """
        if not isinstance(nx, int):
            raise TypeError("nx must be an integer")
        if nx < 1:
            raise ValueError("nx must be a positive integer")

        """Initialize weights using a normal distribution"""
        self.W = np.random.randn(1, nx)
        self.b = 0  # Bias initialized to zero
        self.A = 0  # Activated output initialized to zero
