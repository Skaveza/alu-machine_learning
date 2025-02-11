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
        self.__W = np.random.randn(1, nx)
        self.__b = 0
        self.__A = 0

    #Private attribute getters
    @property
    def W(self):
        """W Getter"""
        return self.__W

    @property
    def b(self):
        """b Getter"""
        return self.__b

    @property
    def A(self):
        """A Getter"""
        return self.__A
