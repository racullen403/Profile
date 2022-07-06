"""
Given a sorted array of distinct integers, and a target value, we must find the target, if it does not exist,
then we must find the correct insert position of the target value. Solution must be O(logn)


Solution:
    - This is just a very basic binary search method

    - Let mid = (l+r)//2 and move l=mid+1 if nums[mid] < target or r=mid-1 nums[mid] > target. Return mid if
    nums[mid] == target.

    - This means if the target exists, it will be returned before the loop ends. If no target exists, l will always
    end on the index where it should be.

        e.g. If no target exists, then we will always end up with the following cases


            Case 1: [a, b] where l points to a and r points to b

                    If target < a then after loop, r will point to l-1, so l points to a and loop ends.

                    If a < target then after loop, l=r, and we get Case 2.


            Case 2: [a] where l and r point to same place a

                    If target < a then after loop, r=l-1 and loop will end.

                    If target > a then after loop, l = l+1 and loop will end.

            We see in each of these cases, l ends up at the position the target should have been found.
"""


def search_insert(nums, target):
    if len(nums) == 0:
        return 0
    l, r = 0, len(nums)-1
    while l <= r:
        mid = (l+r)//2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid+1
        else:
            r = mid-1
    return l

