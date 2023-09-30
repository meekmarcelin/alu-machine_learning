#!/usr/bin/env python3
""" Mathematical Approximations """


π = 3.1415926536
e = 2.7182818285


class Poisson:
    def __init__(self, data=None, lambtha=1.):
        if data is not None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(sum(data) / len(data))
        else:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)

    def pmf(self, k):
        # Convert k to an integer
        k = int(k)

        # Check if k is out of range (negative or not an integer)
        if k < 0 or not isinstance(k, int):
            return 0

        # Calculate the Poisson PMF value for k
        import math
        pmf_value = (self.lambtha ** k) * (math.exp(-self.lambtha) / math.factorial(k))
        return pmf_value
