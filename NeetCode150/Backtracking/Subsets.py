"""
Medium: Given array of unique integers nums, return all possible subsets of nums. Solution cannot contain suplicates.

Sol:
    - Do a dfs through the nums creating a path along the way that we add to the result output at each step.
"""

def subsets(nums):
    res = [[]]

    def dfs(i, path):
        print("i:", i, "path:", path)
        for j in range(i, len(nums)):
            new = path + [nums[j]]
            print("  new:", new)
            res.append(new)
            dfs(j + 1, new)

    dfs(0, [])
    print("SUBSETS:", res)
    return res

def test():
    subsets([1, 2, 3])

test()
               