#!/usr/bin/env python3
"""Normalization """
import numpy as np


def normalize(X, m, s):
    """Returns mean and standard deviation of input data"""
    m = m.reshape((-1, 1))
    s = s.reshape((-1, 1))
    X -= m
    X /= s
    return X
