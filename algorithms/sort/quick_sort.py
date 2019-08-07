"""
Quick sort

Sort list/array arr by partitioning all elems in arr around
a partition element. 
"""

def quick_sort(arr, asc=True):
    """
    Input:
    - arr - list of ints to sort
    - asc - bool. True for ascending, False for descending

    Outputs:
    - List of sorted ints
    """
    pass


import random
unsorted = [random.randint(0, 1000) for i in range(0, 9)]

print(quick_sort(unsorted))
print(quick_sort(unsorted, False))
