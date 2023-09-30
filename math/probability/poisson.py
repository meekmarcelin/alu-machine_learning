#!/usr/bin/env python3
"""Poisson distribution class."""

π = 3.1415926536
e = 2.7182818285

class Poisson:
    """
    Class to represent a Poisson distribution.

    Attributes:
        lambtha (float): Expected number of occurrences in a given time frame.
    """

    def __init__(self, data=None, lambtha=1.):
        """
        Initialize a Poisson distribution.

        Args:
            data (list): List of data to estimate the distribution.
            lambtha (float): Expected number of occurrences.

        Raises:
            ValueError: If lambtha is not a positive value or equals 0.
            TypeError: If data is not a list or does not contain at least two data points.
        """
        if data is not None:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.lambtha = float(sum(data) / len(data))
        else:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)

    def pmf(self, k):
        """
        Calculate the value of the PMF for a given number of successes.

        Args:
            k (int or float): The number of successes.

        Returns:
            float: The PMF value for k.
        """
        # Convert k to an integer
        k = int(k)

        # Check if k is out of range (negative or not an integer)
        if k < 0:
            return 0

        # Calculate the Poisson PMF value for k
        import math
        pmf_value = (self.lambtha ** k) * (math.exp(-self.lambtha) / math.factorial(k))
        return pmf_value

# Test the Poisson class
if __name__ == "__main__":
    import numpy as np
    np.random.seed(0)
    data = np.random.poisson(5., 100).tolist()
    p1 = Poisson(data)
    print('P(9):', p1.pmf(9))

    p2 = Poisson(lambtha=5)
    print('P(9):', p2.pmf(9))
