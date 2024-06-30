"""
Given an array of integers and a target (always exists and is unique), we want to return the
indices of 2 elements that add to give the target.

Solution 1:
    There is the obvious brute force computation method:
    - For every item we look for the other item that would add to give the target, this would
    take O(n^2) time
    - 2*Sn =    1     +  2     + ... + (n-2) + (n-1) + n
                (n-1) +  (n-2) + ... + 2     + 1     + n

        Sn = (n^2)/2

Solution 2:
    The more elegant solution is the one pass method using a lookup map:
    - For each item we check if (target-item) is in a lookup table, if it is, we can
    return the index stored in the lookup table and the current item index, if it's not, then we add the
    current item and its index into the table, then continue to the next item.
    - This method would at worst take O(n) time, and O(n) space

    e.g [2, 3, 1, 5, 4, 6] target=6 lookup={}

        6-2=4, 4 not in lookup so lookup={2:0}
        6-3=3, 3 not in lookup so lookup={2:0, 3:1}
        6-1=5, 5 not in lookup so lookup={2:0, 3:1, 1:2}
        6-5=1, 1 is in the lookup, so return the indices of 1 and 5, e.g [2, 3]

"""


def two_sum(nums, target):
    lookup = {}
    for i in range(len(nums)):
        if (target - nums[i]) in lookup:
            return i, lookup[target-nums[i]]
        lookup[nums[i]] = i


def example_two_sum():
    a = [1, 3, 5, 2, 8, 11]
    targets = [4, 6, 9, 16, 11]
    for tar in targets:
        answer = two_sum(a, tar)
        print("Target:", tar, "Indices:", answer, "Nums:", a[answer[0]], "+", a[answer[1]])

