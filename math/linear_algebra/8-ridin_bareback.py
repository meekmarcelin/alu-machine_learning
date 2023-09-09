#!/usr/bin/env python3
def mat_mul(mat1, mat2):
    # Check if the matrices can be multiplied (the number of columns in mat1
    # must be equal to the number of rows in mat2)
    if len(mat1[0]) != len(mat2):
        return None
    
    # Initialize an empty result matrix
    result = []
    
    # Perform matrix multiplication
    for i in range(len(mat1)):
        row = []
        for j in range(len(mat2[0])):
            dot_product = sum(mat1[i][k] * mat2[k][j] for k in range(len(mat1[0])))
            row.append(dot_product)
        result.append(row)
    
    return result

if __name__ == "__main__":
    mat1 = [[1, 2],
            [3, 4],
            [5, 6]]
    mat2 = [[1, 2, 3, 4],
            [5, 6, 7, 8]]
    
    result = mat_mul(mat1, mat2)
    print(result)
