#!/usr/bin/env python3

""" calculate the shape of a matrix function"""


def np_shape(matrix):
    """Find the matrix shape"""
    import numpy as np
    shape = np.shape(matrix)
    return shape
