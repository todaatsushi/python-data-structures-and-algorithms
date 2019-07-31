"""
Jump Search.

Search a sorted array/list by skipping through an array in x sized intervals. When
the value at xn is larger than the target, linear search for the value.
"""

def jump_search(arr, x, value):
    """
    Input:
    - Arr is a list of ints
    - x is the size of the jump interval
    - value is the target value.

    Returns (index, value) or -1 if value not found.
    """
    arr = sorted(arr)
    index = x
    size = len(arr) - 1

    while True:
        # if index is bigger than the length
        if index > size:
            # if the last value is smaller than target value, target value not found
            if arr[size] < value:
                return -1
            # else iterate back through the final values and search
            else:
                index = size - x
                for i in range(index, size):
                    if arr[i] == value:
                        return (i, arr[i])
                return -1
        
        # Get value at xn steps
        current = arr[index]
        
        # if current is target value, return index and value
        if current == value:
            return (index, value)
        # elif current is larger
        elif current > value:
            # iterate back to xn - x steps and find value or not found
            for i in range(index - x, index):
                if arr[i] == value:
                    return (i, arr[i])
            else:
                return -1
        # else
        else:
            # Add x to index
            index += x

print(jump_search([ 2, 3, 4, 10, 40 ], 2, 10))
print(jump_search([ 2, 3, 4, 10, 40 ], 2, 100))
