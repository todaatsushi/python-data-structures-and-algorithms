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
    pass


txt = 'ababcabcabababd'
pat = 'ababd'
print(kmp_search(txt, pat))
