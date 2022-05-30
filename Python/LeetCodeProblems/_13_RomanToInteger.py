"""
We want to convert a string of Roman Numerals into the corresponding
integer

Solution:
    - We simply have a pointer that moves along the numerals O(n).
    - If the previous numeral before the pointer is larger than the current, then
    we subtract the current numeral, else add the numeral.
    - Note that the last numeral will always be added
"""


def roman_to_integer(s):
    if len(s) == 0:
        return 0
    lookup = {"M": 1000,
              "D": 500,
              "C": 100,
              "L": 50,
              "X": 10,
              "V": 5,
              "I": 1
              }
    total = lookup[s[len(s)-1]]
    i = len(s)-2
    while i >= 0:
        if lookup[s[i]] < lookup[s[i+1]]:
            total -= lookup[s[i]]
        else:
            total += lookup[s[i]]
        i -= 1
    return total
