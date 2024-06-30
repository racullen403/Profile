"""
Given array of integers nums, return the element that appears more than floor(n/2) times, ie majority element.

Trie to solve in O(n) time and O(1) space

Sol:
    We can build a solution using a dictionary to store element:count pairs, and compare the, to floor(n/2). However,
    this will be an O(n) memory solution.


Sol 2: Moore's Voting Approach

    We can find a candidate for the majority element, in one pass, using Moore's Voting Approach. We simply choose
    candidate:count pair from the first element (ie count nums[0]:1), and linearly go through all the elements. If
    an element is the same as candidate, add 1 to count, if it is different, subtract 1. When we reach count 0 and
    the next element is different from the candidate, we restart from here (ie nums[i]:1) and continue as before.

    This method will give the solution because we know there is a majority element, in the case where we are not
    certain, we would need to go through the list once more and count the occurrences of the final candidate.

    e.g
            nums = A A A B B C C A C A B A A,  n = 13

            There are 7 occurrences of A and 6 occurrences of not A, hence, regardless of the arrangement of elements,
            we will always result in an A:1 final count.

"""


def majority_element(nums):
    lookup = {}
    for i in range(len(nums)):
        if nums[i] not in lookup:
            lookup[nums[i]] = 1
        else:
            lookup[nums[i]] += 1
        if lookup[nums[i]] > len(nums)//2:
            return nums[i]


def moores_voting_approach(nums):
    num = nums[0]
    count = 1
    for i in range(1, len(nums)):
        if nums[i] == num:
            count += 1
        elif count == 0:
            num = nums[i]
            count = 1
        else:
            count -= 1
    return num

