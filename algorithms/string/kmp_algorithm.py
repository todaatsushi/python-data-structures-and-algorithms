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
    pi = [
        {
            'letter': pat[i],
            'value': 0
        } for i in range(len(pat))
    ]
    ## brute force search for repeating prefix in the suffix
    # Loop over pat
    for n in range(1, len(pat)):
        value_counter = 1
        index = n

        # loop over pattern find matches to prefix of pattern
        # increment the value as number of matches increases
        # continue until mismatch
        for i in range(len(pat)):
            if pat[index] == pat[i]:
                pi[index]['value'] = value_counter
                value_counter += 1
                index += 1
            else:
                value_counter = 1
                index = n
                break

    # add a start point at the beginning of the pi table
    pi.insert(0, 'start')
    print(pi)

    # Return object
    indicies = []

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
