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
    if size > 1:
        # split into left and right
        middle_index = floor(size / 2)
        left = unsorted[0:middle_index]
        right = unsorted[middle_index:size]
        print(left, right)
        # sort both left and right halves
        left, right = merge_sort(left, asc), merge_sort(right, asc)
        print(left, right)
    else:
        return unsorted
    # Else just return single element

    # Merge two halves via insertion sort
    # return


import random
unsorted = [random.randint(0, 1000) for i in range(0, 9)]

print(merge_sort(unsorted))
# print(merge_sort(unsorted, False))
