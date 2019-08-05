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
    sorted_list = []
    unsorted_list = list(arr)

    while len(unsorted_list) is not 0:
        current = unsorted_list.pop(
            unsorted_list.index(min(unsorted_list))
        )
        sorted_list.insert(len(sorted_list), current)

    if not asc:
        desc_list = []
        for i in sorted_list:
            desc_list.insert(0, i)
        return desc_list
    return sorted_list


import random
to_sort = [random.randint(0, 1000) for i in range(0, 10)]

print(selection_sort(to_sort))
print(selection_sort(to_sort, False))
