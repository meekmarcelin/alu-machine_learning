#!/usr/bin/env python3
dd_arrays(arr1, arr2):
    if len(arr1) != len(arr2):
        return None

    # Initialize an empty list to store the result
    result = []

    # Iterate through the elements of arr1 and arr2 and add them element-wise
    for i in range(len(arr1)):
        result.append(arr1[i] + arr2[i])

    return result

