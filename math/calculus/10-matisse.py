#!/usr/bin/env python3
"This module calculates the derivative of a polynomial"


def poly_derivative(poly):
  "returns derivative of a polynomial"
  if not isinstance(poly, list):
    return None

  if len(poly) == 1:
    return [0]

    derivative = []
    for power, coef in enumerate(poly[1:], start=1):
        derivative.append(coef * power)

    return derivative if any (derivative) else [0]
  