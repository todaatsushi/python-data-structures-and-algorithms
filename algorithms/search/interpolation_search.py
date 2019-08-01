"""
Interpolation search.

Search sorted and uniformly distributed array/list arr for element x.
"""

def get_index(arr, start, end):
    """
    Returns int index of the start position to carry out interpolation search.

    Inputs:
    - Arr - array of ints
    """
    # workout index with formula
    index = (start + (
        (end - start) / (arr[start] - arr[end])
        ) * (
            end - arr[start]
        )
    )
    return index