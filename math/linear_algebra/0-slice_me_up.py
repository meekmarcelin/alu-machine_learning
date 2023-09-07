#!/usr/bin/env python3

"""
This script slices and displays specific parts of an array.
"""

# Define the array
arr = [9, 8, 2, 3, 9, 4, 1, 0, 3]

# Slice the array to get the required parts and print the results
print("The first two numbers of the array are: {}".format(arr[:2]))
print("The last five numbers of the array are: {}".format(arr[-5:]))
print("The 2nd through 6th numbers of the array are: {}".format(arr[1:6]))

