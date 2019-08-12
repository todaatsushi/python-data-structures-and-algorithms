"""
Knuth–Morris–Pratt algorithm

Searches string txt for string pat but avoid wasted time by mapping repeating patterns
in pat and creating a pi table to avoid rematching already matched portions of txt.
"""

def kmp_search(txt, pat):
    """
    Input:
    - txt - string to search in for pat.
    - pat - string to search pat for

    Output:
    - list of ints containing starting indicies for pat.

    Returns empty string if pat doesn't exist.
    """
    # Create pi table - all vals to set to 0 initially
    ## brute force search for repeating prefix in the suffix
    # Loop over pat
        # if letter matches first letter of pat, change value to 1
        # if next letter matches the next letter of pat, change value to 2
        # continue until mismatch
    # add a start point at the beginning of the pi table

    ## Algorithm
    # Loop over txt
        # If letter matches first letter in pat
        # Log starting index
            # Check next letter
            # Continue until mismatch
        ## Mismatch
            # revert pattern index to the value index assigned to the
            # letter in the pi table
    # if word is matched, add starting index to return list
    # else return empty list
    pass


txt = 'ababcabcabababd'
pat = 'ababd'
print(kmp_search(txt, pat))
