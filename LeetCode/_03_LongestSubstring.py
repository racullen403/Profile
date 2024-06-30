"""
For this task we are given a string, and must find the longest substring that
does not contain repeating characters.

Solution:
    - The solution for this is to use a left and a right pointer to indicate the
    current pattern we are looking at, and have a lookup table that lets us
    know if the next character is in the pattern already or not.
    - We move the right pointer through the string, if we come across a character already in the lookup and
    if the index of the character is >= l, then we know it is a repeating character, so we move our left pointer
    up to this repetition and continue.
    - Note that we will always iterate through the whole string in O(n) time and at worst the space needed for the
    lookup will also we O(n)

"""


def longest_substring(s):
    l = 0
    count = 0
    lookup = {}
    for r in range(len(s)):
        if s[r] not in lookup:
            count = max(count, r-l+1)
        else:
            if lookup[s[r]] < l:
                count = max(count, r-l+1)
            else:
                l = lookup[s[r]]+1
        lookup[s[r]] = r
    return count


