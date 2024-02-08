#!/usr/bin/env python3
"""Moving average"""

def moving_average(data, beta):
    """
    Calculates the weighted moving average of a dataset.

    Args:
    data: List of data points to calculate the moving average of.
    beta: Weight used for the moving average.

    Returns:
    List containing the moving averages of the input data.
    """
    # Initialize variables
    moving_avg = []
    v_hat = 0
    
    # Calculate moving averages
    for i in range(len(data)):
        v_hat = beta * v_hat + (1 - beta) * data[i]
        bias_correction = 1 - beta ** (i + 1)
        moving_avg.append(v_hat / bias_correction)
    
    return moving_avg
