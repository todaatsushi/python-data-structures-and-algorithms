"""
Naive algorithm for pattern searching

Given text txt and a pattern pat, returns a list of indicies
where pat appears in txt.
"""

def naive_pattern_match(txt, pat):
    """
    Input:
    - txt, pat - strings where txt is the string to search
    and pat is string to find within txt

    Output:
    - List of ints, where each int indicates where in txt pat
    appears.
    """
    if not pat:
        raise ValueError('Pattern must not be empty!')
    # Get intial variables
    indicies = []
    first_letter = pat[0]

    # Cycle through txt
    for n in range(0, len(txt)):
        # compare current letter with first letter to pattern match
        current = txt[n]
        if current == first_letter:
            match = True
            # If they match, cycle through the rest of the pattern
            for i in range(0, len(pat)):
                # Break if letters don't match / if we run out of word
                try:
                    if pat[i] != txt[n + i]:
                        match = False
                        break
                except IndexError:
                    match = False
                    break
            # if flag is still true, add the initial index to the list
            if match:
                indicies.append(n)
    return indicies


txt = 'AABAACAADAABAABA'
pat = 'AABA'
print(naive_pattern_match(txt, pat))
