"""
Exponential search.

Searches list/array arr for element x where binary search is performed
given a range of elements to search over.
"""
# reuse binary search
from binary_search import binary_search

def exponential_search(arr, x):
    """
    Input:
    - arr - sorted array of ints
    - x - int - value to be found

    Returns (index, x) where index is the index of x in arr.
    If x is not in arr, returns -1.
    """
    # Base case
    if arr[0] == x:
        return (0, x)
    
    index = 1
    arr_len = len(arr)

    # Calculate bounds of the arr to search
    # Check if index is out of bounds and if value if too small
    while index < arr_len and arr[index] <= x:
        if arr[index] == x:
            return (index, arr[index])
        index *= 2

    return binary_search(arr, index / 2, min(index, len(arr) - 1), x)

success = [
    [1, 2, 4, 4, 5, 6, 7, 7, 9, 9, 10, 11, 12, 15, 21, 44, 100],
    44
]

print('\nExponential search results:')
print(exponential_search(success[0], success[1]))
print(exponential_search(success[0], 103))
