""" 
Medium: Given an array of distinct integers nums, and a target integer, create unique combinations from the list that add to give target.
We can use the same number muliple times. Note that [1, 2] and [2, 1] count at the same. Nums are positive.

Sol:
    - Sort the array 
"""

def combinationSum(nums, target):
    res = []

    def dfs(i, path, total):
        if total == target:
            res.append(path.copy())
        elif total < target:
            for j in range(i, len(nums)):
                dfs(j, path + [nums[j]], total + nums[j])
        
    dfs(0, [], 0)

    return res