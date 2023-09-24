#!/usr/bin/env python3
"""Sum or total"""


def summation_i_squared(n):
    """Summation"""
    # Check (integer)
    if not isinstance(n, int) or n < 1:
        return None

    # Base case: when n reaches 1, return 1^2 = 1
    if n == 1:
        return 1
    # Sum of natural numbers
    return (n*(n+1)*(2*n+1))/6
