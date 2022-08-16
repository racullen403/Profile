"""
Sequential  searching starting from one end and checking every element until an element is found.

Searching is O(n) and space is O(_01_BasicPython)
"""


# Simple Algorithm to search for element x in an array arr
def linear_search(arr, x, show=False):
    if show is True:
        print("\n----Linear Search----")
        print("Searching for: ", x)
    for i in arr:
        if i == x:
            if show is True:
                print("Found: ", i)
                print("----End----")
            return i
    if show is True:
        print("Could not find ", x)
        print("----End----")
    return -1

a = [1, 2, 3, 4, 5, 6]
linear_search(a, 3, True)
linear_search(a, 8, True)