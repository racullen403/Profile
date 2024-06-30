"""
Given an array nums, we want to rotate all the elements, in place, by k steps to the right.

    e.g     nums = [1, 2, 3, 4, 5, 6, 7]    k = 3

            output = [5, 6, 7, 1, 2, 3, 4]


Solution:
    The best way to solve this is by thinking about how the rotation is shifting the last k elements to the first
    k positions every time. In the way, we split the array into 2 sub arrays

    [1, 2, 3, 4] and [5, 6, 7] where k = 3 above

    now reverse the sub arrays and then the complete array

    [4, 3, 2, 1, 7, 6, 5] -> [5, 6, 7, 1, 2, 3, 4]
"""


def rotate_array(nums, k):
    if k > len(nums):
        k = k % len(nums)

    def reverse(l, r):
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

    reverse(0, len(nums) - k - 1)
    reverse(len(nums) - k, len(nums) - 1)
    reverse(0, len(nums) - 1)

    return nums


def test():
    nums = [1, 2, 3, 4, 5, 6, 7, 8]
    print(rotate_array(nums, 9))


test()
