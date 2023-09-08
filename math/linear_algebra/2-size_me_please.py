#!/usr/bin/env python3


"""
2-size_me_please.py
A module for calculating the shape of a matrix.
"""
def matrix_shape(matrix):
    shape = []
    while isinstance(matrix, list):
        shape.append(len(matrix))
        matrix = matrix[0]
    return shape
