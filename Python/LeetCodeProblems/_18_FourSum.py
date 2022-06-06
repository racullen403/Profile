"""
We are tasked with finding every collection of 4 elements from a list that add to give
some target (we can't use the same index more than once)

N-Sum Problem:
    - This 4-sum and previous 3-sum can be broken down into an N-sum problem, where we reduce the problem
    until be reach the 2-sum.
    - During the reduction, we keep track of the new target value, and check against certain conditions to ensure
    a solution is even possible.
    - Ensure the array is sorted and consider the following:

        - if n < 2 we have gone too far
        - if len(nums) < n then we can't find a solution
        - if num[0]*n > target then we cannot find a solution
        - if num[-1]*n < target then we cannot find a solution
"""


def find_4_sum(nums, target):
    nums.sort()
    output = []
    findNsum(4, nums, target, [], output)
    return output


def find_n_sum(n, nums, target, path, output):
    if n < 2 or len(nums) < n or nums[0]*n > target or nums[-1]*n < target:
        return
    elif n > 2:
        for i in range(len(nums)-n+1):
            if i == 0 or (i > 0 and nums[i-1] != nums[i]):
                findNsum(n-1, nums[i+1:], target-nums[i], path+[nums[i]], output)
    else:
        l = 0
        r = len(nums)-1
        while l < r:
            total = nums[l] + nums[r]
            if total == target:
                output.append(result + [nums[l], nums[r]])
                while l < r and nums[l] == nums[l+1]:
                    l += 1
                while l < r and nums[r] == nums[r-1]:
                    r -= 1
                l += 1
                r -= 1
            elif total < target:
                l += 1
            else:
                r -= 1
    return


