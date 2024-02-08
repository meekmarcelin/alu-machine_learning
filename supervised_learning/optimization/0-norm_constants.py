#!/usr/bin/env python3
""" constant normalization """
import numpy as np


def normalize_constants(x):
    """ Return mena and standard deviation """
 mean = np.mean(X, axis=0)
 std_dev = np.std(X, axis=0)

 return mean, std_dev   