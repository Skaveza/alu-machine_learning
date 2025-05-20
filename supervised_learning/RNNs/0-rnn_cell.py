#!/usr/bin/env python3
"""
Mmodule initializes a class that represents an RNN cell 
"""


import numpy as np

class RNNCell:
    def __init__(self, i, h, o):
        """
        Initialize the RNNCell.

        Parameters:
        i (int): Dimensionality of the data.
        h (int): Dimensionality of the hidden state.
        o (int): Dimensionality of the output.
        """
        # Weight matrix for hidden state
        self.Wh = np.random.randn(i + h, h)

        # Bias for hidden state
        self.bh = np.zeros((1, h))

        # Weight matrix for output
        self.Wy = np.random.randn(h, o)

        # Bias for output: shape
        self.by = np.zeros((1, o))

    def forward(self, h_prev, x_t):
        """
        Performs forward propagation for one time step.

        Parameters:
        h_prev (ndarray): Previous hidden state, shape (m, h)
        x_t (ndarray): Input data at time t, shape (m, i)

        Returns:
        h_next (ndarray): Next hidden state, shape (m, h)
        y (ndarray): Output at time t, shape (m, o)
        """
        # Concatenate h_prev and x_t along last dimension
        concat = np.concatenate((h_prev, x_t), axis=1)

        # Compute next hidden state using tanh activation
        h_next = np.tanh(np.matmul(concat, self.Wh) + self.bh)

        # Compute output before activation
        raw_y = np.matmul(h_next, self.Wy) + self.by

        # Apply softmax activation
        y = np.exp(raw_y) / np.sum(np.exp(raw_y), axis=1, keepdims=True)

        return h_next, y
