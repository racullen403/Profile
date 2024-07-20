"""
Medium: Given array of unique integers, return all possible permutations.

Sol:
    - Simply build up the solutions by carrying through the remaining integers not yet added.
"""

def permutations(nums):
    res = []
    nums = set(nums)

    def dfs(path, choices):
        print("path", path, "choices", choices)
        if not choices:
                res.append(path.copy())
                print("  append")
                return
        choices_copy = choices.copy()
        for n in choices_copy:
            choices.remove(n)
            print("  n", n, "choices", choices)
            dfs(path + [n], choices)
            choices.add(n)
    
    dfs([], nums)

    return res


def test():
    print(permutations([1, 2, 3]))

test()