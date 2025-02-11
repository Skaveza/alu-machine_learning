#!/usr/bin/env python3
"""This module defines a Neuron class for performing binary classification"""


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

    # Private attribute Getters
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


    def forward_prop(self, X):
      """
      Calculates the forward propagation of the neuron.
      
      Parameters:
      X (numpy.ndarray): input data with shape (nx, m).
      nx is the number of input features to the neuron.
      m is the number of examples.
      
      Returns:
      numpy.ndarray: The activated output of the neuron:
      """
      
      #Compute the linear combiantion to get Z
      Z =np.dot(self._W, X) + (self._b)
      
      #Apply sigmoid activation function
      self._A = 1 /(1 + np.exp(-Z))
      
      return self._A
    
    
    

