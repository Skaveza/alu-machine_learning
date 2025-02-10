#!/usr/bin/env python3
"""
Module calculates the polsterior probability"""


import numpy as np
from scipy.special import comb


def likelihood(x, n, P):
    """Calculate the likelihood of obtaining the data given P"""
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

    # Binomial coefficient
    binom_coeff = comb(n, x)

    # Likelihood calculation for each probability in P
    likelihoods = binom_coeff * (P ** x) * ((1 - P) ** (n - x))

    return likelihoods


def intersection(x, n, P, Pr):
    """
    Calculate the intersection of obtaining the data
    """
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
    if not isinstance(Pr, np.ndarray) or Pr.shape != P.shape:
        raise TypeError("Pr must be a numpy.ndarray with the same shape as P")
    if np.any(P < 0) or np.any(P > 1):
        raise ValueError("All values in P must be in the range [0, 1]")
    if np.any(Pr < 0) or np.any(Pr > 1):
        raise ValueError("All values in Pr must be in the range [0, 1]")
    if not np.isclose(np.sum(Pr), 1):
        raise ValueError("Pr must sum to 1")

    # Likelihood calculation
    L = likelihood(x, n, P)

    # Intersection (likelihood * prior for each probability)
    intersection_values = L * Pr

    return intersection_values


def marginal(x, n, P, Pr):
    """Calculate the marginal probability of obtaining the data."""
    # Input validation (same as in the intersection function)
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

    # Calculate intersection
    intersection_values = intersection(x, n, P, Pr)

    # Marginal probability is the sum of intersection values
    marginal_prob = np.sum(intersection_values)

    return marginal_prob


def posterior(x, n, P, Pr):
    """
    Calculate the posterior probability for the various hypothetical
    probabilities of developing severe side effects given the data.

    Parameters:
    x (int): Number of patients with severe side effects.
    n (int): Total number of patients.
    P (numpy.ndarray): 1D array of probabilities of severe side effects.
    Pr (numpy.ndarray): 1D array of prior beliefs about P.

    Returns:
    numpy.ndarray: Posterior probabilities of each value in P given x and n.
    """
    # Input validation (same as in the previous functions)
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
    if not isinstance(Pr, np.ndarray) or Pr.shape != P.shape:
        raise TypeError("Pr must be a numpy.ndarray with the same shape as P")
    if np.any(P < 0) or np.any(P > 1):
        raise ValueError("All values in P must be in the range [0, 1]")
    if np.any(Pr < 0) or np.any(Pr > 1):
        raise ValueError("All values in Pr must be in the range [0, 1]")
    if not np.isclose(np.sum(Pr), 1):
        raise ValueError("Pr must sum to 1")

    # Calculate likelihood for each probability in P
    L = likelihood(x, n, P)

    # Calculate marginal probability
    marginal_prob = marginal(x, n, P, Pr)

    # Posterior calculation
    posterior_probs = (L * Pr) / marginal_prob

    return posterior_probs
