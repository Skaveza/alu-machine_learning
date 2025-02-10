#!/usr/bin/env python3
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

        # Private attributes
        self.__W = np.random.randn(1, nx)  # Weight vector
        self.__b = 0  # Bias
        self.__A = 0  # Activated output

    # Getters for private attributes
    @property
    def W(self):
        """Getter for W"""
        return self.__W

    @property
    def b(self):
        """Getter for b"""
        return self.__b

    @property
    def A(self):
        """Getter for A"""
        return self.__A
