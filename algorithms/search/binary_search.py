"""
Binary Search

Search a sorted array/list by repeatedly dividing the search interval in half.
"""

def binary_search(arr, start, end, x):
    """
    Input:
    - Arr is a python list of ints
    - x is the target value

    Returns x if found or returns -1.
    """
    import math

    if start <= end:
        arr = sorted(arr)
        middle_index = int(math.floor((start + end) / 2))
        middle_value = arr[middle_index]

        if middle_value == x:
            return (middle_index, middle_value)
        if len(arr) == 1:
            return -1
        elif middle_value > x:
            return binary_search(arr, start, middle_index - 1, x)
        elif middle_value < x:
            return binary_search(arr, middle_index + 1, end, x)
    return -1

arr = [ 2, 3, 4, 10, 40 ]
start = 0
end = len(arr) - 1

# Sucess
print(binary_search(arr, start, end, 10))

# Fail
print(binary_search(arr, start, end, 100))
