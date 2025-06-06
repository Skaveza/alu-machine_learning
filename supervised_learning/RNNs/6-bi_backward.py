#!/usr/bin/env python3
"""Importing numpy"""
import numpy as np


class BidirectionalCell:
    """
    Represents bidirectional cell of
    RNN
    """
    def __init__(self, i, h, o):
        """
        Class constructor
        """
        self.Whf = np.random.normal(size=(h + i, h))
        self.Whb = np.random.normal(size=(h + i, h))
        self.Wy = np.random.normal(size=((2 * h), o))
        self.bhf = np.zeros((1, h))
        self.bhb = np.zeros((1, h))
        self.by = np.zeros((1, o))

    def forward(self, h_prev, x_t):
        """
        Performs forward prop
        """
        h_x = np.concatenate((h_prev, x_t), axis=1)
        h_next = np.tanh(np.matmul(h_x, self.Whf) + self.bhf)
        return h_next

    def backward(self, h_next, x_t):
        """
        Caclculate hidden state in backward
        direction for one time step
        """
        h_x = np.concatenate((h_next, x_t), axis=1)
        h_prev = np.tanh(np.matmul(h_x, self.Whb) + self.bhb)
        return h_prev
