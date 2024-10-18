#!/usr/bin/env python3
"""
Module calculates the intersection
"""


import numpy as np
from scipy.special import comb


def likelihood(x, n, P):
    """Calculate the likelihood of obtaining the data given P"""
    # Input validation (same as before)
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")
    if not isinstance(x, int) or x < 0:
        raise ValueError("x must be >= 0")
    if x > n:
        raise ValueError("x cannot be greater than n")
    if not isinstance(P, np.ndarray) or P.ndim != 1:
        raise TypeError("P must be a 1D numpy.ndarray")
    if np.any(P < 0) or np.any(P > 1):
        raise ValueError("All values in P must be in the range [0, 1]")

    # Calculate binomial coefficient
    binom_coeff = comb(n, x)
    
    # Calculate the likelihood for each probability in P
    likelihoods = binom_coeff * (P ** x) * ((1 - P) ** (n - x))

    return likelihoods

def intersection(x, n, P, Pr):
    """
    Calculate the intersection of obtaining the data with the various
    hypothetical probabilities.
    
    Parameters:
    x (int): Number of patients with severe side effects.
    n (int): Total number of patients.
    P (numpy.ndarray): 1D array of probabilities of severe side effects.
    Pr (numpy.ndarray): 1D array of prior beliefs of P.
    
    Returns:
    numpy.ndarray: Intersection of obtaining x and n with each probability in P.
    """
    # Input validation
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")
    if not isinstance(x, int) or x < 0:
        raise ValueError("x must be >= 0")
    if x > n:
        raise ValueError("x cannot be greater than n")
    if not isinstance(P, np.ndarray) or P.ndim != 1:
        raise TypeError("P must be a 1D numpy.ndarray")
    if not isinstance(Pr, np.ndarray) or Pr.shape != P.shape:
        raise TypeError("Pr must be a numpy.ndarray with the same shape as P")
    if np.any(P < 0) or np.any(P > 1):
        raise ValueError("All values in P must be in the range [0, 1]")
    if np.any(Pr < 0) or np.any(Pr > 1):
        raise ValueError("All values in Pr must be in the range [0, 1]")
    if not np.isclose(np.sum(Pr), 1):
        raise ValueError("Pr must sum to 1")
    
    # Calculate likelihoods using the previous function
    L = likelihood(x, n, P)

    # Calculate intersection (likelihood * prior for each probability)
    intersection_values = L * Pr

    return intersection_values
