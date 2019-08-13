"""
Rabin-Karp algorithm.

Search string txt for string pat using the Rabin-Karp algorithm where a hash function is used
to generate a hash code for pat. The hash code is used to find the pattern in txt.
"""


def get_hash(pat):
    """
    Using ascii values as the hash values for each character in pat,
    returns a hash code where the ascii values of pat are totalled.

    Inputs:
    - pat - string to get code for. Assumes pat is a string.

    Outputs:
    - Int hash code.
    """
    code = 0
    for char in pat:
        code += ord(char)

    return code


def rabin_karp_algorithm(txt, pat):
    """
    Inputs:
    txt - string of which we search for pat.
    pat - string of which we search for in txt.

    Output:
    Returns a list of indicies in txt where pat appears.
    Returns empty list if no matches are found.
    """
    # Get hash code of pat
    pat_value = get_hash(pat)
    pat_size = len(pat)
    txt_size = len(txt)

    ## Rolling hash function
    current = ''
    start_index = 0
    indicies = []

    # Iterate through txt
    for i in range(txt_size - 2):
        # Construct txt substring
        for n in range(pat_size):
            current += txt[i + n]
        # Use hash function and get the hash code of the current substring
        current_value = get_hash(current)
        match = True

        if current_value == pat_value:
            # if the hash code matches
            for x in range(pat_size):
                # Iterate through the string and check the values match
                if pat[x] != current[x]:
                    match = False
                    break
            # Log the start index
            if match:
                indicies.append(start_index)

        # Carry on cycling
        current = ''
        start_index = i + 1
        if start_index == txt_size:
            break
    # Return
    return indicies

txt = 'aaaaab'
pat = 'aab'
print(rabin_karp_algorithm(txt, pat))
