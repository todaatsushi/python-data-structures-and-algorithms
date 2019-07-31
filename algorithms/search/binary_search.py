"""
Binary Search

Search a sorted array/list by repeatedly dividing the search interval in half.
"""

def binary_search(arr, x):
    """
    Input:
    - Arr is a python list of ints
    - x is the target value

    Returns x if found or raises error.
    """
    import math
    arr = sorted(arr)
    middle_index = int(math.floor(len(arr) / 2))
    middle_value = arr[middle_index]

    if middle_value == x:
        return x
    elif len(arr) == 1:
        raise IndexError("Value not found.")
    elif middle_value > x:
        return binary_search(arr[0:middle_index], x)
    elif middle_value < x:
        return binary_search(arr[middle_index:], x)

print(binary_search([ 2, 3, 4, 10, 40 ], 10))
print(binary_search([ 2, 3, 4, 10, 40 ], 100))
