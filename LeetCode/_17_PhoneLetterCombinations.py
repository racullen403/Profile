"""
We want to make all possible letter combinations on a phone, that a string of digits would produce

Solution 1, Recursive Approach:
    - We can solve this quite simply using a dfs recursive algorithm
    - There will be roughly 3**n combinations (or 3**n * 4**m, where n is no. of 3 letter digits
    and m is no. of 4 letter digits)


Solution 2, Dynamic Approach:
    - We iterate over the string of digits
    - For each digit, we create a temporary empty list and append the old
    strings+new_character into the temporary list.
    - We then update this temporary list to be the output, and repeat for the next digit
"""


# Solution 1
def letter_combos_recursive(digits):
    if len(digits) == 0:
        return []

    # DFS for find letter combinations
    def dfs_path(ind, path, solutions):
        if ind < len(digits):
            for i in range(len(lookup[digits[ind]])):
                dfs_path(ind + 1, path + lookup[digits[ind]][i], solutions)
        else:
            solutions.append(path)

    lookup = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }
    output = []
    dfs_path(0, "", output)
    return output


# Solution 2
def letter_combos_dynamic(digits):
    if len(digits) == 0:
        return ""
    lookup = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz"
    }
    combos = [""]
    for i in range(len(digits)):
        new_combos = []
        for c in combos:
            for j in range(len(lookup[digits[i]])):
                new_combos.append(c + lookup[digits[i]][j])
        combos = new_combos
    return combos
