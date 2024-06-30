"""
Given an integer array nums, sorted in ascending order, find the start and final indices of a target number in
O(logn) time, return [-1, -1] if target does not exist.


Solution:

    - We can solve this using 2 binary searches, one to find the left side of the target number interval, and
    one to find its right side

    - Left side:

            [1, 1, 1, 3, 3, 4] consider finding the left side for target 3

            - pointer l will need to stop moving once it reaches the first 3, If nums[mid] < 3, l = mid + 1

            - pointer r will need to keep moving left, until it lies to the left of l, If nums[mid] >= 3, r = mid - 1

            - In this way, l will stop at the correct left side and r will end the loop when r < l.

    - Right side uses similar logic:

            - pointer r will need to move left until it stops at the right most target number,
            If nums[mid] > target, r = mid - 1

            - pointer l will keep moving to the right, If nums[mid] <= target, l = mid+1

            - continue  until l > r, stopping the loop.

    - In the case where the target value does not exist, the left side binary search will give the first number
    larger than the target, l1, and the right side binary search will return the first number smaller than the
    target, r2. This means if l1 > r2, return [-1, -1]

"""


def find_first_last_position(nums, target):
    l1, l2, r1, r2 = 0, 0, len(nums)-1, len(nums)-1
    # Binary Search for left side, given by l1
    while l1 <= r1:
        mid = (l1+r1) // 2
        if nums[mid] < target:
            l1 = mid+1
        else:
            r1 = mid - 1
    # Binary Search for right side, given by r2
    while l2 <= r2:
        mid = (l2+r2) // 2
        if nums[mid] <= target:
            l2 = mid + 1
        else:
            r2 = mid - 1
    if l1 <= r2:
        return [l1, r2]
    return [-1, -1]
