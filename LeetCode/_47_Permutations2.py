"""
Given a collection of numbers, nums, that might contain duplicates, return all possible unique permutations
in any order.


Solution:

    - This is very similar to _46_Permutations, except, we need to consider that there are non-unique numbers in
    nums.
    - To take care of this we need to preprocess the input, one way would be to sort it and then ensure when adding
    to the "path", we are not creating the same path as previously, this can be done by ensuring nums[i] != nums[i-1]
    when we place a new value into the permutation.
    - The way I have done it simply counts the occurrences of each number into a dictionary, we then build
    up permutations while the count > 0.
"""


def permutations_2(nums):
    # Set up counter for all numbers in nums
    counts = {}
    for num in nums:
        if num not in counts:
            counts[num] = 0
        counts[num] += 1

    # Hold solutions
    solutions = []

    # DFS with backtracking
    def dfs_solve(path):
        if len(path) == len(nums):
            solutions.append(path[:])
        else:
            for key in counts.keys():
                if counts[key] > 0:
                    counts[key] -= 1
                    path.append(key)
                    dfs_solve(path)
                    path.pop()
                    counts[key] += 1

    dfs_solve([])

    return solutions

