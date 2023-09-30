#!/usr/bin/env python3

# Mathematical Approximations
π = 3.1415926536
e = 2.7182818285

class Poisson:
    """
    Poisson class represents a Poisson distribution.
    """

    def __init__(self, data=None, lambtha=1.):
        if data is None:
            if lambtha <= 0:
                raise ValueError("lambtha must be a positive value")
            self.lambtha = float(lambtha)
        else:
            if not isinstance(data, list):
                raise TypeError("data must be a list")
            if len(data) < 2:
                raise ValueError("data must contain multiple values")
            self.lambtha = float(sum(data) / len(data))

if __name__ == "__main__":
    # Sample code
    data = [4, 3, 6, 8, 2]
    p1 = Poisson(data)
    print('Lambtha:', p1.lambtha)

    p2 = Poisson(lambtha=5)
    print('Lambtha:', p2.lambtha)
