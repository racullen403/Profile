"""
Given a string, s, of parenthesis "(" and ")", we want to return the longest substring that has well-formed
parenthesis.


Solution:

    - We can do this in linear time as follows.
    - Let bp = [], be an empty list that will contain the indices of "break points". We say a break point is the index
    of a character that does not form a valid parenthesis. In this way, the gaps between break points will give the
    lengths of valid parenthesis.

    - Iterating through the indices i of string s, if s[i] is "(" we add it to the bp list

    - If s[i] is ")" then we have 3 cases:

        - If bp is empty then add i to bp
        - If bp is not empty and the last entry, bp[-1] points to "(", then pop the last bp out.
        - If bp is not empty and bp[-1] is ")", then it forms another break point and add it to bp

    - Finally, go through the bp list, and return the largest length between break points.

"""


def longest_valid_substring_parenthesis(s):
    # Form "Break Point" list
    bp = []
    for i in range(len(s)):
        if s[i] == "(":
            bp.append(i)
        elif len(bp) == 0:
            bp.append(i)
        elif s[bp[-1]] == "(":
            bp.pop()
        else:
            bp.append(i)
    # Add the len(s) as a final term in bp, this lets us compare last bp to the end length
    bp.append(len(s))
    # Set the first length at bp[0], this gives the initial valid length
    longest = bp[0]
    for i in range(len(bp)-1):
        length = bp[i+1] - bp[i] - 1
        if length > longest:
            longest = length
    return longest

