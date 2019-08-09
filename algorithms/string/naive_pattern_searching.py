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
    pass

txt = 'AABAACAADAABAABA'
pat = 'AABA'
print(naive_pattern_match(txt, pat))
