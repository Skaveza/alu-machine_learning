#!/usr/bin/env python3

"""This module defines a single Neuron that performs binary classification"""


import numpy as np

class Neuron:
  """Defines a Neurons that performs binary classification"""

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
         raise ValueError("nx must be a postive integer")

#Private attributes
self.__W = random.randn
self.__b = 0
self.__A = 0

#Private Attribute Getters
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
  Calculates the forward propagation of the neuron
  X(numpy.ndarray) with shape (nx, m): where nx is the number of input neurons
                                       and m is the number of examples.
                                       
  Returns:
  numpy.ndarray:the activated output of the neuron
  """

# Performing dot product to get Z
Z = np.dot(self.__W, X) + self.__b

#Sigmoid Activation function
self.__A = 1(1 + np.exp(-Z))

return self.__A

def cost(self, Y, A):
  """
  Calculates the cost of the model using logistic regression
  Y(numpy.ndarray) with shape (1,m) that contains correct labels for the input data
  A(numpy.ndarray) with shape (1,m) containing the activated output of the neuron for each example

  Returns:
  float: The cost of the model
  """
  m = Y.shape[1]
  cost = -np.sum(Y * np.log(A) + (1 - Y) * np.log(1.0000001 - A)) / m
  return cost
