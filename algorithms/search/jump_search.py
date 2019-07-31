"""
Jump Search.

Search a sorted array/list by skipping through an array in x sized intervals. When
the value at xn is larger than the target, linear search for the value.
"""

def jump_search(arr, x, value):
    arr = sorted(arr)
    index = x

    while True:
        # if index is bigger than the length
            # if the last value is smaller than target value, target value not found
            # else iterate back through the final values and search
        
        # Get value at xn steps
        # if current is target value, return index and value
        # elif current is larger
            # iterate back to xn - x steps and find value or not found
        # else
            # Add x to index
            # continue loop
        pass
