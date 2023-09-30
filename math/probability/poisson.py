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

        from poisson import Poisson  # Corrected import statement
import numpy as np

np.random.seed(0)
data = np.random.poisson(5., 100).tolist()
p1 = Poisson(data)
print('P(9):', p1.pmf(9))

p2 = Poisson(lambtha=5)
print('P(9):', p2.pmf(9))
