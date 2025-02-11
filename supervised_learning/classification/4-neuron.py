#!/usr/bin/env python3


"""This module defines a single Neuron that performs binary classification"""

import numpy as np


class Neuron:
    """Defines a Neuron that performs binary classification"""

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

    # Private Attribute Getters
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
        X (numpy.ndarray): Input data with shape (nx, m).
        nx is the number of input features.
        m is the number of examples.

        Returns:
        numpy.ndarray: The activated output of the neuron.
        """
        Z = np.dot(self.__W, X) + self.__b
        self.__A = 1 / (1 + np.exp(-Z))
        return self.__A

    def cost(self, Y, A):
        """
        Calculates the cost of the model using logistic regression.

        Parameters:
        Y (numpy.ndarray) with shape (1,m).
        Contains correct labels for the input data.
        A (numpy.ndarray) with shape (1, m).
        Contains the activated output of the neuron for each example.

        Returns:
        float: The cost of the model.
        """
        m = Y.shape[1]
        cost = -np.sum(Y * np.log(A) + (1 - Y) * np.log(1.0000001 - A)) / m
        return cost

    def evaluate(self, X, Y):
        """
        Evaluates the neuron's predictions.

        Parameters:
        X(numpy.ndarray): (nx, m), contains input data.
        nx: the number of input features to the neuron.
        m: the number of examples.

        Y(numpy.ndarray): (1,m), contains correct labels of input data

        Returns:
        tuple: A tuple containing:
              - numpy.ndarray, the predicted labels for each example(1,m).
              -float: cost of the model.
        """

        # Perform forward propagation to calculate the activated output
        A = self.forward_prop(X)

        # Generate binary predictions: 1 if A >= 0.5 else 0
        predictions = np.where(A >= 0.5, 1, 0)

        # Calculate the cost using the cost function
        cost = self.cost(Y, A)

        return predictions, cost
