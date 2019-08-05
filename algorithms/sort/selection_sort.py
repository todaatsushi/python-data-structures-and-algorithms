"""
Selection Sort

Sorts array/list arr by repeatedly finding the min element from the unsorted section of
arr, and putting it at the beginning.
"""

def selection_sort(arr, asc=True):
    """
    Input:
    - Unsorted list of ints
    - Bool indicating ascending (True) or descending (False)

    Outputs:
    - Sorted version of list of ints.
    """
    # Return variable
    sorted_list = []
    unsorted_list = list(arr)

    # Keep taking min value out of unsorted_list until all values are taken
    while len(unsorted_list) is not 0:
        current = unsorted_list.pop(
            unsorted_list.index(min(unsorted_list))
        )

        # Add to the end of the sorted array for ascending, beginning if descending
        sorted_list.insert(
            len(sorted_list) if asc else 0,
            current
        )

    return sorted_list


import random
to_sort = [random.randint(0, 1000) for i in range(0, 10)]

print(selection_sort(to_sort))
print(selection_sort(to_sort, False))
