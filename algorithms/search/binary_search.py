"""
Binary Search

Search a sorted array/list by repeatedly dividing the search interval in half.
"""

def binary_search(arr, x):
    import math
    arr = sorted(arr)
    middle_index = int(math.floor(len(arr) / 2))
    middle_value = arr[middle_index]

    if middle_value == x:
        return x
    elif middle_value > x:
        return binary_search(arr[0:middle_index], x)
    elif middle_value < x:
        return binary_search(arr[middle_index:], x)
    else:
        raise IndexError("Value not found.")

print(binary_search([ 2, 3, 4, 10, 40 ], 10))
