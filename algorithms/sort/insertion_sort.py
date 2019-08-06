"""
Insertion sort.

Sort list/array arr of ints and sort it by iterating through and placing each element
where it should be.
"""

def insertion_sort(arr, asc=True):
    """
    Inputs:
    - Arr - list of ints to be sorted. Assumes arr
    is longer than 1 element long.
    - asc - True for ascending, False for descending
    """
    final = list(arr)

    # Iterate through list
    for i in range(1, len(final)):
        current = final[i]

        # Compare current to every preceding element
        for n in range(0, i):

            # If smaller, place before and remove current from current location
            if current < final[n]:
                final.pop(i)
                final.insert(n, current)
                break

    # Reverse list for descending order
    if not asc:
        return [final[i] for i in range(len(final) - 1, -1, -1)]

    return final


import random
unsorted = [random.randint(0, 1000) for i in range(0, 10)]

print(insertion_sort(unsorted))
print(insertion_sort(unsorted, False))
