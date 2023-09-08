#!/usr/bin/env python3
def matrix_transpose(matrix):
    num_rows = len(matrix)
    num_columns = len(matrix[0])
    transpose_matrix = [[0 for _ in range(num_rows)] for _ in range(num_columns)]
    for i in range(num_rows):
        for j in range(num_columns):
            transpose_matrix[j][i] = matrix[i][j]

    return transpose_matrix
