"""
Medium: Given an array of integers, nums, that may contain duplicates. Return all possible subsets.

Sol:
    - Sort the array so that we can build subsets like before, but skip terms that are the same as previous to avoid permutations.
"""

def subsetWithDup(nums):
    nums.sort()
    res = [[]] 

    def dfs(path, i):
        if i == len(nums):
            return
        for j in range(i, len(nums)):
            if j > i and nums[j] == nums[j - 1]:
                continue
            res.append(path + [nums[j]])
            dfs(path + [nums[j]], j + 1)
    
    dfs([], 0)
    print(res)

    return res



def test():
    subsetWithDup([1, 2, 1])

test()