"""
Linear search implementation.

Given an array/list arr of n elements, write a function to search a given element x in arr.
"""
import sys

def linear_search(arr, x):
    try:
        return arr.index(x)
    except ValueError:
        return -1

print(linear_search([10, 20, 80, 30, 60, 50, 110, 100, 130, 170], 110))
print(linear_search([10, 20, 80, 30, 60, 50, 110, 100, 130, 170], 175))
