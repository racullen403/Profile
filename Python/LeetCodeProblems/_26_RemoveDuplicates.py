"""
Given an array of non-decreasing numbers, we must return the array so that the first k elements are unique (where k
is the number of unique elements in the array).

Solution:
    - Keep a set as a lookup to see if element is unique
    - Iterate through the array with a pointer for the position the next element should be place. If the element is
    in the lookup set, go next, else add it to the set, place element at the pointer position and move the pointer
    forward one position
    - Note this solution is a general solution for any array of numbers, we are told the array is non-decreasing, so
    we could also just compare the element to its previous, if it hasn't increased then we know it's a duplicate. The
    advantage of this is we don't have to store the set containing uniques, which at worst case would be O(n) space.

"""


# Solution 1, general
def remove_duplicates(nums):
    lookup = set()
    pos = 0
    for i in range(len(nums)):
        if nums[i] not in lookup:
            nums[pos] = nums[i]
            pos += 1
            lookup.add(nums[i])
    pos -= 1
    return nums, pos


# Solution 2, non-decreasing
def remove_duplicates_non_decreasing(nums):
    pos = 1
    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            nums[pos] = nums[i]
            pos += 1
    pos -= 1
    return nums, pos

