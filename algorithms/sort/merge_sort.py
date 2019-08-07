"""
Merge sort

Divides array/list arr into 2 halves, sorts the two halves, and then
merges the two sorted halves.
"""
from insertion_sort import insertion_sort


def merge(arr1, arr2, asc=True):
    """
    Merges two lists arr1 and arr2 of ints into one in
    either ascending or descending order.

    Inputs:
    - arr1, arr2 - lists of ints
    - asc - bool, True for ascending, False for descending

    Outputs:
    - Returns sorted list if ints
    """
    arr1.extend(arr2)
    return insertion_sort(
        arr1,
        asc
    )


def merge_sort(arr, asc=True):
    """
    Input:
    - arr - unsorted list of ints
    - asc - True for ascending, False for descending

    Returns
    - Sorted list
    """
    from math import floor
    unsorted = list(arr)
    size = len(arr)
    
    # If size is bigger than 1    
    if size > 1:
        # split into left and right
        middle_index = floor(size / 2)
        left = unsorted[0:middle_index]
        right = unsorted[middle_index:size]
        # sort both left and right halves
        left, right = merge_sort(left, asc), merge_sort(right, asc)
    else:
        # Else just return single element
        return unsorted

    # Merge two halves via insertion sort
    merged = merge(left, right, asc)

    # Reverse if desc
    if not asc:
        return [merged[i] for i in range(len(merged) - 1, -1, -1)]
    return merged


import random
unsorted = [random.randint(0, 1000) for i in range(0, 9)]

print('\nMerge sort results:\n')
print(merge_sort(unsorted))
print(merge_sort(unsorted, False))
