#!/usr/bin/env python3
def matrix_transpose(matrix):
    num_rows = len(matrix)
    num_columns = len(matrix[0])
    transpose_matrix = [[0 for _ in range(num_rows)] for _ in range(num_columns)]
    for r in range(num_rows):
        for c in range(num_columns):
            transpose_matrix[c][r] = matrix[r][c]

    return transpose_matrix
