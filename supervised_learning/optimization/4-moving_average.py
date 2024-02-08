#!/usr/bin/env python3
"""Moving average"""


def moving_average(data, beta):
    # Initialize variables
    moving_avg = []
    v_hat = 0
    
    # Calculate moving averages
    for i in range(len(data)):
        v_hat = beta * v_hat + (1 - beta) * data[i]
        bias_correction = 1 - beta ** (i + 1)
        moving_avg.append(v_hat / bias_correction)
    
    return moving_avg
