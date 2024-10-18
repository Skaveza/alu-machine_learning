#!/usr/bin/env python3
"""
Module calculates posterior probability within a range
"""


from scipy import special


def posterior(x, n, p1, p2):
    """
    Calculate the posterior probability that p is within the range [p1, p2]

    Parameters:
    x (int): Number of patients with severe side effects.
    n (int): Total number of patients.
    p1 (float): Lower bound on the range.
    p2 (float): Upper bound on the range.

    Returns:
    float: Posterior probability that p is within the range [p1, p2].
    """
    # Input validation
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")
    if not isinstance(x, int) or x < 0:
        raise ValueError("x must be an integer that is greater than or equal to 0")
    if x > n:
        raise ValueError("x cannot be greater than n")
    if not isinstance(p1, float) or not (0 <= p1 <= 1):
        raise ValueError("p1 must be a float in the range [0, 1]")
    if not isinstance(p2, float) or not (0 <= p2 <= 1):
        raise ValueError("p2 must be a float in the range [0, 1]")
    if p2 <= p1:
        raise ValueError("p2 must be greater than p1")

    # Calculate the Beta (CDF)
    beta_cdf_p1 = special.betainc(x + 1, n - x + 1, p1)
    beta_cdf_p2 = special.betainc(x + 1, n - x + 1, p2)

    #posterior probability is the difference between the two CDF values
    posterior_prob = beta_cdf_p2 - beta_cdf_p1

    return posterior_prob
