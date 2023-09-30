def __init__(self, data=None, lambtha=1.):
    """
    Initialize an Exponential distribution.

    Args:
        data (list): List of data to estimate the distribution.
        lambtha (float): Expected number of occurrences.

    Raises:
        ValueError: If lambtha is not a positive value.
        TypeError: If data is not a list or does not contain at least two data points.
    """
    if data is not None:
        if not isinstance(data, list):
            raise TypeError("data must be a list")
        if len(data) < 2:
            raise ValueError("data must contain multiple values")
        self.lambtha = 1 / (
            sum(data) / len(data)
        )
    else:
        if lambtha <= 0:
            raise ValueError("lambtha must be a positive value")
        self.lambtha = float(lambtha)
