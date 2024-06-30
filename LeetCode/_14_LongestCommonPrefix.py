"""
We want to return the longest common prefix from a list of strings

Solution:
    - We find the smallest word in the list
    - We then iterate through the letters of this word and compare to the rest of the list
"""


def longest_common_prefix(strings):
    shortest = min(strings, key=len)
    output = ""
    i = 0
    while i < len(shortest):
        for word in strings:
            if word[i] != shortest[i]:
                return output
        output += shortest[i]
        i += 1
    return output

