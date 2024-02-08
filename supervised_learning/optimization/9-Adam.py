#!/usr/bin/env python3
"""Update variables Adam"""
import numpy as np


def update_variables_Adam(alpha, beta1, beta2, epsilon, var, grad, v, s, t):
    """
    Updates a variable using the Adam optimization algorithm.

    Args:
    alpha: Learning rate.
    beta1: Weight used for the first moment.
    beta2: Weight used for the second moment.
    epsilon: Small number to avoid division by zero.
    var: Numpy array containing the variable to be updated.
    grad: Numpy array containing the gradient of var.
    v: Numpy array containing the previous first moment of var.
    s: Numpy array containing the previous second moment of var.
    t: Time step used for bias correction.
    """
    v = (beta1 * v) + (1 - beta1) * grad
    v_c = v / (1 - (beta1 ** t))

    s = (beta2 * s) + (1 - beta2) * (grad ** 2)
    s_c = s / (1 - (beta2 ** t))

    var -= (alpha * (v_c / (np.sqrt(s_c) + epsilon)))

    return var, v, s
