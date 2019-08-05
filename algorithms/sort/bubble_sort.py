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
    # Return variable
    final_list = list(arr)

    # Flag variable
    no_swaps = True

    while True:
        for i in range(0, len(final_list)):
            # Compare current and next values
            current = final_list[i]

            # Break loop if at the end of the list
            try:
                next = final_list[i + 1]
            except IndexError:
                break

            # Swap places of the two elements if current is larger
            if current > next:
                final_list[i] = next
                final_list[i + 1] = current
                
                # Flag constraint fail
                no_swaps = False
        
        # No swaps means list is in order so break loop
        if no_swaps:
            break
        # Otherwise reassume default position
        no_swaps = True

    # Reverse the list if we wanted descending
    if not asc:
        return [final_list[i] for i in range(len(final_list) - 1, -1, -1)]
    
    return final_list

import random
arr = [random.randint(0, 1000) for i in range(0, 6)]

print(bubble_sort(arr, True))
print(bubble_sort(arr, False))
