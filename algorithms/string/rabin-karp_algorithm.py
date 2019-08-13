"""
Rabin-Karp algorithm.

Search string txt for string pat using the Rabin-Karp algorithm where a hash function is used
to generate a hash code for pat. The hash code is used to find the pattern in txt.
"""

def rabin_karp_algorithm(txt, pat):
    """
    Inputs:
    txt - string of which we search for pat.
    pat - string of which we search for in txt.

    Output:
    Returns a list of indicies in txt where pat appears.
    """
    pass

txt = 'aaaaab'
pat = 'aab'
print(rabin_karp_algorithm(txt, pat))
