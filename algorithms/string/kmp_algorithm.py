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
    ## Create pi table - all vals to set to 0 initially
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

    # Return object
    indicies = []

    ## Algorithm
    # Loop over txt
    txt_index = 0
    start_index = 0
    pat_index = 0
    size = len(txt)

    # Loop over pat
    while txt_index < size:
        # Get place in txt
        text = txt[txt_index]
        pattern = pi[pat_index]['letter']
        # If letter matches first letter in pat check next letter
        if text == pattern:
            # If at the end of pattern it is a match
            if pat_index == len(pat) - 1:
                indicies.append(start_index)
                start_index = txt_index + 1
                pat_index = -1
            # If at the end of txt, return indicies
            if txt_index == len(txt) - 1:
                return indicies
            
            # Check next letter
            pat_index += 1
        # else move onto next letter
        ## Mismatch
        else:
            # Start a new match pattern
            start_index = txt_index + 1

            # revert pattern index to the value index assigned to the
            pat_index = pi[pat_index]['value']
            
            # letter in the pi table

        txt_index += 1
    # if word is matched, add starting index to return list
    # else return empty list
    return indicies


txt = 'ababcabcabababd'
pat = 'ababd'
print(kmp_search(txt, pat))
