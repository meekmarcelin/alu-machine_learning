#!/usr/bin/env python3

# Mathematical Approximations
from poisson import Poisson
π = 3.1415926536
e = 2.7182818285

class Poisson:
    """
    Poisson class represents a Poisson distribution.
    
    Class constructor __init__(self, data=None, lambtha=1.):
    - data is a list of the data to be used to estimate the distribution.
    - lambtha is the expected number of occurrences in a given time frame.
    - Sets the instance attribute lambtha.
    - Saves lambtha as a float.
    - If data is not given (i.e., None), it uses the given lambtha.
    - If lambtha is not a positive value or equals to 0, it raises a ValueError with the message lambtha must be a positive value.
    - If data is given:
      - Calculates the lambtha of data.
      - If data is not a list, it raises a TypeError with the message data must be a list.
      - If data does not contain at least two data points, it raises a ValueError with the message data must contain multiple values.
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

    np.random.seed(0)
    data = np.random.poisson(5., 100).tolist()
    p1 = Poisson(data)
    print('Lambtha:', p1.lambtha)

    p2 = Poisson(lambtha=5)
    print('Lambtha:', p2.lambtha)
