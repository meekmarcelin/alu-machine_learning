#!/usr/bin/env python3
def add_arrays(arr1, arr2):
    # Check if the input arrays have the same length
    if len(arr1) != len(arr2):
        return None

    # Initialize an empty list to store the result
    result = []

    # Iterate through the elements of arr1 and arr2 and add them element-wise
    for i in range(len(arr1)):
        result.append(arr1[i] + arr2[i])

    return result

if __name__ == "__main__":
    arr1 = [1, 2, 3, 4]
    arr2 = [5, 6, 7, 8]
    print(add_arrays(arr1, arr2))
    print(arr1)
    print(arr2)
    print(add_arrays(arr1, [1, 2, 3]))


