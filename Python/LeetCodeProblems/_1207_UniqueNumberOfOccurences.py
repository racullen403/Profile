"""
Given an array of integers, we want to know if there is a unique number of occurrences of each integer.

    e.g [1, 2, 2, 3, 3, 3] would return True, there are 3 3's, 2 2'2 and 1 1.

        [1, 2, 3] would return False, there is 1 1, 1 2, and 1 3


    Solution 1:
        - We could simply count the number of occurrences of each integer, and then iterate through these counts,
        if we find 2 counts the same, return False
        - We will have to iterate through the n integers and then the m unique integers, so runtime will be O(n)

"""


def unique_occurrences(array):
    counts = {}
    for num in array:
        if num not in counts:
            counts[num] = 0
        counts[num] += 1
    uniques = set()
    for count in counts.values():
        if count in uniques:
            return False
        uniques.add(count)
    return True


def example():
    a1 = [1, 2, 3]
    a2 = [1, 1, 2, 3, 3, 3]
    print("Array", a1, ":", unique_occurrences(a1))
    print("Array", a2, ":", unique_occurrences(a2))


example()