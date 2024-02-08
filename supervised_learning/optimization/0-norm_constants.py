#!/usr/bin/env python3
"""optimization"""
import numpy as np


def normalize_constants(X):
    """ Return mean and standard deviation """
     X_ref = X.copy()
    m, nx = X_ref.shape
    mean = (1 / m) * X_ref.sum(axis=0)
    X_ref -= mean
    X_ref = X_ref ** 2
    var = (1 / m) * X_ref.sum(axis=0)
    dv = np.sqrt(var)
    return mean, dv
