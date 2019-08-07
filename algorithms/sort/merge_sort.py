"""
Merge sort

Divides array/list arr into 2 halves, sorts the two halves, and then
merges the two sorted halves.
"""

def merge_sort(arr, asc=True):
    """
    Input:
    - arr - unsorted list of ints
    - asc - True for ascending, False for descending

    Returns
    - Sorted list
    """
    pass

import random
unsorted = [random.randint(0, 1000) for i in range(0, 10)]

print(merge_sort(unsorted))
print(merge_sort(unsorted, False))
