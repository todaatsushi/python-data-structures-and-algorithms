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
    from math import floor
    print(arr)
    unsorted = list(arr)
    size = len(arr)

    # If size is bigger than 1
        # split into left and right
        # sort both left and right halves
    # Else just return single element

    # Merge two halves via insertion sort
    # return


import random
unsorted = [random.randint(0, 1000) for i in range(0, 9)]

print(merge_sort(unsorted))
# print(merge_sort(unsorted, False))
