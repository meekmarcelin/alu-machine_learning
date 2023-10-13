#!/usr/bin/env python3

def determinant(matrix):
    """
    Calculate the determinant of a square matrix.

    Args:
        matrix (list of lists): The input matrix.

    Returns:
        float: The determinant of the input matrix.

    Raises:
        TypeError: If the input is not a list of lists.
        ValueError: If the input is not a square matrix.
    """
    if not isinstance(matrix, list) or not all(isinstance(row, list) for row in matrix):
        raise TypeError("matrix must be a list of lists")

    # Check if the matrix is square
    num_rows = len(matrix)
    if num_rows == 0:
        return 1.0  # A 0x0 matrix is considered to have a determinant of 1
    if not all(len(row) == num_rows for row in matrix):
        raise ValueError("matrix must be a square matrix")

    # Base case for 1x1 matrix
    if num_rows == 1:
        return float(matrix[0][0])

    # Base case for 2x2 matrix
    if num_rows == 2:
        return float(matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0])

    det = 0.0
    for j in range(num_rows):
        # Calculate the cofactor matrix
        cofactor_matrix = [[matrix[i][k] for k in range(num_rows) if k != j]
                          for i in range(1, num_rows)]
        # Add the determinant of the current element multiplied by the cofactor determinant
        det += float(matrix[0][j] * ((-1) ** j) * determinant(cofactor_matrix))

    return det

if __name__ == '__main__':
    mat0 = [[]]
    mat1 = [[5]]
    mat2 = [[1, 2], [3, 4]]
    mat3 = [[1, 1], [1, 1]]
    mat4 = [[5, 7, 9], [3, 1, 8], [6, 2, 4]]
    mat5 = []
    mat6 = [[1, 2, 3], [4, 5, 6]]

    print(determinant(mat0))
    print(determinant(mat1))
    print(determinant(mat2))
    print(determinant(mat3))
    print(determinant(mat4))
    try:
        determinant(mat5)
    except Exception as e:
        print(e)
    try:
        determinant(mat6)
    except Exception as e:
        print(e)
