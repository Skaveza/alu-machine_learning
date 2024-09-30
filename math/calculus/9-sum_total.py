#!/usr/bin/env python3
"This module is used to calculate the sum of squares"

def summation_i_squared(n):
  "Calculates the sum of squares from 1 to n"
  return sum(i**2 for i in range(1, n+1))
    