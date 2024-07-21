"""
Medium: Given array of integers nums, which may contain duplicates, and a target integer, return a list of unique combinations 
of nums that sum to target.

Sol:
    - Same method as combination sum, just sort the array first, and when creating new subsets, skip values that would lead to same result.

"""

def combinationSum2(nums, target):
    nums.sort()
    res = []

    def backtrack(i, path, total):
        if total == target:
            res.append(path.copy())
        if i == len(nums) or total > target:
            return
        for j in range(i, len(nums)):
            if j > i and nums[j] == nums[j - 1]:
                continue
            else:
                backtrack(j + 1, path + [nums[j]], total + nums[j])

    backtrack(0, [], 0)

    return res