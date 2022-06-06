"""
Given the following pairs pf parenthesis, () {} [], we have to determine if a string/equation
has valid parenthesis.

Solution:
    - We will use a lookup/dictionary to determine if the character is a parenthesis (ignore
    other terms as we assume them to be digits or operators)
    - Append opening parenthesis into a stack
    - When we come across a closing parenthesis we have a few possibilities:

        -The stack is empty, in which case the parenthesis has no opening and is invalid.
        -The stack is not empty, we pop the last opening parenthesis from the stack, if it
        is not the correct opening for the closing parenthesis, then it is not valid.

    - Finally we compare the stack == [], if it is empty then the parenthesis were valid,
    if not, then we have openings with no closing so not valid.
"""


def is_valid_parenthesis(s):
    lookup = {"{": "}",
              "[": "]",
              "(": ")"
              }
    stack = []
    for ch in s:
        if ch in lookup.keys():
            stack.append(ch)
        elif ch in lookup.values() and (stack == [] or lookup[stack.pop()] != ch):
            return False
    return stack == []

