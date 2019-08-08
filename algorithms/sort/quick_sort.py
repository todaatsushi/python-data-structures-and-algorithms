"""
Quick sort

Sort list/array arr by recursively partitioning all elems in arr around
a pivot element. 
"""

def quick_sort(arr, asc=True):
    """
    Input:
    - arr - list of ints to sort
    - asc - bool. True for ascending, False for descending

    Outputs:
    - List of sorted ints
    """
    size = len(arr)
    pivot = arr[0]

    # Base case
    if size == 1:
        return arr

    left, right = 0, size -1
    no_swap = False

    while left < right:
        # find left
        # Increment left until we find an element greater than pivot
        while not arr[left] > pivot:
            left += 1
            if left == size:
                break

        # decremenet right until element is smaller than or equal to pivot
        while not arr[right] <= pivot:
            right -= 1
            if right == 0:
                if left == size:
                    no_swap = True
                break

        if no_swap:
            no_swap = False
        elif left > right:
            break
        else:
            arr[left], arr[right] = arr[right], arr[left]

    # Swap pivot right right elem
    arr[0], arr[right] = arr[right], arr[0]
    
    # split arr at new pivot location i.e. right
    if size == 2:
        pass
    else:
        split_point = arr.index(arr[right])
        arr[0:right] = quick_sort(arr[0:right])
        arr[right + 1:size + 1] = quick_sort(arr[right + 1:size + 1])

    return arr
        
            

    
                


import random
# unsorted = [15, 3, 9, 8, 5, 2, 7, 1, 6]
unsorted = [10, 16, 8, 12, 15, 6, 3, 9, 5]

# unsorted = [random.randint(0, 20) for i in range(0, 6)]
quick = quick_sort(unsorted)
print(quick)

# print(quick_sort(unsorted, False))
