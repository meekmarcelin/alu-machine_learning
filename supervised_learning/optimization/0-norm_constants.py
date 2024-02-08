#!/usr/bin/env python3
"""optimization"""
import numpy as np

def normalize_constants(X):
    """ Return mean and standard deviation """
    mean = np.mean(X, axis=0)
    std_dev = np.std(X, axis=0)
    return mean, std_dev
