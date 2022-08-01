"""
Given an array, nums, of distinct integers, return all the possible permutations.
You can return the answer in any order.


Solution:

    - We can solve this very easily using a recursive dfs. We will simply swap terms into positions to make up the
    permutations.

        E.G.    Take [1, 2, 3] for every position, we swap every term into it and then move to the next position

                index = 0

                    [1, 2, 3] [2, 1, 3] [3, 2, 1] Now index pos 0 is complete, we got to index 1 and swap every higher
                    index term into it

                index = 1

                    [1, 2, 3] [1, 3, 2]  [2, 1, 3] [2, 3, 1]  [3, 2, 1] [3, 1, 2]

                    again, we move the index up 1 and swap every index term equal of higher in to the position

                index = 2

                    [1, 2, 3] [1, 3, 2]  [2, 1, 3] [2, 3, 1]  [3, 2, 1] [3, 1, 2] Final solution

    - Note:  when solving this with dfs, we use backtracking to revert the array after a swap has occurred, this
    way, after an iteration in the for loop, the next iteration uses the same input array and not the final one
    produced by the dfs.
"""


def permutations(nums):
    solutions = []

    def dfs_permute(path, numbers, index):
        if len(path) == len(nums):
            solutions.append(path)
        else:
            for i in range(index, len(nums)):
                numbers[i], numbers[index] = numbers[index], numbers[i]
                dfs_permute(path + [numbers[index]], numbers, index + 1)
                numbers[index], numbers[i] = numbers[i], numbers[index]

    dfs_permute([], nums, 0)
    return solutions

