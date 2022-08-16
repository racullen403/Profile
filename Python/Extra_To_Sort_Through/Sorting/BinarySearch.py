"""
Algorithm for finding an element in a sorted array.

Working:
    - Set two pointers at the start and end of an array.
    - Find the middle element m
    - If element we are looking for return it, if less than m, apply binary search to lower
    half of array up to m, if greater then m apply binary search to upper half of array from m.
    - Repeat until we find the element or the two pointers are equal and element isn't there.

Complexity O(logn) on average and worst case, O(_01_BasicPython) on best.
"""


# Recursion method for binary search
def binary_search_func(arr, x, l, r, show=False):
    # Final check is when l = r = m, after this l > r and we end
    if l > r:
        if show is True:
            print("Could not find: ", x)
        return
    m = (l+r)//2
    if show is True:
        print("Searching for {} between {} - {} at ind {}".format(x, arr[l], arr[r], m))
    if arr[m] == x:
        if show is True:
            print("Found: ", arr[m])
        return True
    # note that once l = m, we only have two
    elif x < arr[m]:
        binary_search_func(arr, x, l, m-1, show)
    elif arr[m] < x:
        binary_search_func(arr, x, m+1, r, show)
    return False


def binary_search_recursion(arr, x, show=False):
    if show is True:
        print("\n----Binary Search Recursive----")
    l = 0
    r = len(arr)-1
    binary_search_func(arr, x, l, r, show)
    if show is True:
        print("----End----")


def binary_search_iterative(arr, x, show=False):
    if show is True:
        print("\n----Binary Search Iterative----")
        print("Search", arr, "for ", x)
    l = 0
    r = len(arr) - 1
    m = (l+r)//2
    while l <= r:
        if show is True:
            print("Searching between {} - {} at ind {}".format(arr[l], arr[r], m))
        if arr[m] == x:
            if show is True:
                print("Found: ", arr[m])
                print("----End----")
            return True
        elif x < arr[m]:
            r = m-1
        else:
            l = m+1
        m = (l+r)//2
    if show is True:
        print("Could not find: ", x)
        print("----End----")
    return False


a = [1, 2, 3, 4, 5, 6, 7, 8]
binary_search_recursion(a, 3, True)
binary_search_recursion(a, -1, True)

binary_search_iterative(a, 5, True)
binary_search_iterative(a, 0, True)