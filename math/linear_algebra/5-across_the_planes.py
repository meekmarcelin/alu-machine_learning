#!/usr/bin/env python3
def add_matrices2D(mat1, mat2):
    # Check if the input matrices have the same shape (same number of rows and columns)
    if len(mat1) != len(mat2) or len(mat1[0]) != len(mat2[0]):
        return None

    # Initialize an empty matrix (list of lists) to store the result
    result = []

    # Iterate through the rows of mat1 and mat2 and add them element-wise
    for i in range(len(mat1)):
        row_result = []
        for j in range(len(mat1[0])):
            row_result.append(mat1[i][j] + mat2[i][j])
        result.append(row_result)

    return result

if __name__ == "__main__":
    mat1 = [[1, 2], [3, 4]]
    mat2 = [[5, 6], [7, 8]]
    print(add_matrices2D(mat1, mat2))
    print(mat1)
    print(mat2)
    print(add_matrices2D(mat1, [[1, 2, 3], [4, 5, 6]]))

