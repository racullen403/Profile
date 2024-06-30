"""
We are now given a list of numbers and a target and told to find the closest 3Sum to the
target number

Solution:
    - We pretty much just do the 3Sum solution but store closest values to compare to
"""


def three_sum_closest(nums, target):
    if len(nums) < 3:
        return
    nums.sort()
    closest = nums[0] + nums[1] + nums[2]
    smallest_diff = abs(closest - target)
    for i in range(len(nums) - 2):
        l = i + 1
        r = len(nums) - 1
        while l < r:
            total = nums[i] + nums[l] + nums[r]
            diff = total - target
            if diff < 0:
                l += 1
            elif diff > 0:
                r -= 1
            else:
                return total
            if abs(diff) < smallest_diff:
                smallest_diff = abs(diff)
                closest = total
    return closest
