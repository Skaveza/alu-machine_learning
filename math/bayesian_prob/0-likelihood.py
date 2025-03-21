#!/usr/bin/env python3
"""
Module calculates likelihood
"""


import numpy as np
from scipy.special import comb


def likelihood(x, n, P):
    """
    Calculate the likelihood of obtaining the data

    Parameters:
    x (int): Number of patients with severe side effects.
    n (int): Total number of patients.
    P (numpy.ndarray): 1D array of probabilities of severe side effects.

    Returns:
    numpy.ndarray: Likelihoods of obtaining the data for each probability in P.
    """
    # Input validation
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")
    if not isinstance(x, int) or x < 0:
        raise ValueError(
          "x must be an integer that is greater than or equal to 0"
          )
    if x > n:
        raise ValueError("x cannot be greater than n")
    if not isinstance(P, np.ndarray) or P.ndim != 1:
        raise TypeError("P must be a 1D numpy.ndarray")
    if np.any(P < 0) or np.any(P > 1):
        raise ValueError("All values in P must be in the range [0, 1]")

    # Calculate the binomial coefficient
    binom_coeff = comb(n, x)

    # Calculate the likelihood for each probability in P
    likelihoods = binom_coeff * (P ** x) * ((1 - P) ** (n - x))

    return likelihoods
