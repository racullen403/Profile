"""
Medium: Given a string of digits from 2-9, return the possible letter combinations.

Sol:
    - Basic back tracking algorithm where we insert the final solution into a list.
"""

def letterCombinations(digits):
    lookup = {"2": ["A", "B", "C"],
              "3": ["D", "E", "F"],
              "4": ["G", "H", "I"],
              "5": ["J", "K", "L"],
              "6": ["M", "N", "O"],
              "7": ["P", "Q", "R", "S"],
              "8": ["T", "U", "V"],
              "9": ["W", "X", "Y", "Z"],
              }
    res =[]
    if not len(digits):
        return res
    
    def backtrack(path, digit):
        if len(path) == len(digits):
            res.append(path)
            return
        d = digits[digit]
        for ch in lookup[d]:
            new_path = path + ch.lower()
            backtrack(new_path, digit + 1)
    
    backtrack("", 0)
    return res