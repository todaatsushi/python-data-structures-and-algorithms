"""
Quick sort

Sort list/array arr by partitioning all elems in arr around
a partition element. 
"""

def quick_sort(arr, asc=True):
    """
    Always uses the first element as a pivot.

    Input:
    - arr - list of ints to sort
    - asc - bool. True for ascending, False for descending

    Outputs:
    - List of sorted ints
    """
    # base case - if arr is 1 element long, return element
    # Pick pivot element
    # get endpoints of array
    
    # while left and right haven't met
        # Move left and right points inwards until left element is larger
        # than the pivot elem and right element is smaller
        # Swap values
     
     # split arr where left and right have met
     # call quick_sort on each half

     # flip if descending
     # return
    pass


import random
unsorted = [random.randint(0, 1000) for i in range(0, 9)]

print(quick_sort(unsorted))
print(quick_sort(unsorted, False))
