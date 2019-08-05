"""
Bubble Sort

Sort list/array arr by repeatedly swapping wrongly ordered adjacent elements.
"""

def bubble_sort(arr, asc=True):
    """
    Input:
    - list arr to be sorted (assumes list has at least 2 elements)
    - asc - True to sort ascending, False for descending.

    Output:
    - returns sorted list
    """
    final_list = list(arr)
    no_swaps = True

    while True:
        for i in range(0, len(final_list)):
            current = final_list[i]
            try:
                next = final_list[i + 1]
            except IndexError:
                break
            
            if current > next:
                final_list[i] = next
                final_list[i + 1] = current
                no_swaps = False
        
        if no_swaps:
            break
        no_swaps = True

    if not asc:
        return [final_list[i] for i in range(len(final_list) - 1, -1, -1)]
    
    return final_list

import random
arr = [random.randint(0, 1000) for i in range(0, 6)]

print(bubble_sort(arr, True))
print(bubble_sort(arr, False))
