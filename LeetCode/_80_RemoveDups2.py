"""
Given increasing integer array nums, we want to remove, inplace, integers that result in more than 2 duplicates.

e.g [1, 1, 1, 2, 2, 2] -> [1, 1, 2, 2, x, x]

"""


def remove_dups_2(nums):
    if len(nums) <= 2:
        return nums
    pos = 2
    for i in range(2, len(nums)):
        if nums[i] != nums[pos-1] or nums[pos-1] != nums[pos-2]:
            nums[pos] = nums[i]
            pos += 1
    return nums, pos


def test():
    nums = [1, 1, 1, 2, 2, 2, 3, 4, 5, 5, 6, 7, 7, 7]
    nums2 = [1, 1, 1, 2, 2, 3]
    print(remove_dups_2(nums2))

