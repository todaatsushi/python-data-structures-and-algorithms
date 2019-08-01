"""
Interpolation search.

Search sorted and uniformly distributed array/list arr for element x.
"""

def get_index(arr, start, end, value):
    """
    Returns int index of the start position to carry out interpolation search.

    Inputs:
    - Arr - array of ints
    - start - int: where to start searching
    - end - int: where to end searching
    - value - int: value we are looking for
    """
    import math
    # workout index with formula
    index = start + (end - start) / (arr[end] - arr[start]) * (value - arr[start])
    return int(math.floor(index)) # Ensure right return value format

def interpolation_search(arr, start, end, value):
    """
    Carries out interpolation search on list arr where arr is sorted and uniformly distributed.
    Value should be the search target.

    Returns tuple (index, element) or -1 if value is not found.
    """

    # If array is valid, and target is within the bounds of the array, value may exist within it.
    while start <= end and value >= arr[start] and value <= arr[end]:
        index = get_index(arr, start, end, value)
        current = arr[index]

        if current == value:
            return (index, current)
        elif current < value:
            return interpolation_search(arr, index + 1, end, value)
        elif current > value:
            return interpolation_search(arr, start, index - 1, value)
    return -1


success = ([1, 2, 4, 6, 7, 10, 11, 14, 15], 4)
print(interpolation_search(success[0], 0, len(success[0]) - 1, success[1]))

fail = ([1, 2, 4, 6, 7, 10, 11, 14, 15], 99)
print(interpolation_search(fail[0], 0, len(fail[0]) - 1, fail[1]))
