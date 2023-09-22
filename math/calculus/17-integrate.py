#!/usr/bin/env python3
""" integration """


def poly_integral(poly, C=0):
    # Check if poly is a list and C is an integer
    if not isinstance(poly, list) or not all(isinstance(coeff, (int, float)) for coeff in poly) or not isinstance(C, int):
        return None

    # Initialize the result list with C
    result = [C]

    # Iterate through the coefficients of poly
    for i, coeff in enumerate(poly):
        # Calculate the integral of the term and append to result
        integral_coeff = coeff / (i + 1)
        result.append(integral_coeff)

    return result
