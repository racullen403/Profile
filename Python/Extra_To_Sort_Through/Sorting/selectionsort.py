"""
Selection Sort:
    - Pointer at the first element and pointer for minimum element.
    - Find the minimum element in unsorted array and swap it with the first pointer.
    - Move pointer to the next position and find new minimum element and swap.
    - Repeat for all elements in array

Complexity:
    - Time complexity is always O(n^2) as we have to compare (n-_01_BasicPython)+(n-_01_BasicPython)+...+_01_BasicPython
    everytime.
    - Space complexity O(_01_BasicPython) since we must store the index of min

Unstable
"""


def selection_sort(a, show=False):
    if show is True:
        print("\n----Selection Sort----")
        print("Starting array:", a)
    size = len(a)
    for j in range(size-1):
        min = j
        for i in range(j, size):
            if a[i] < a[min]:
                min = i
        a[j], a[min] = a[min], a[j]
        if show is True:
            print("Swap " + str(j+1) + ": " + str(a))
    if show is True:
        print("Sorted array:", a)
        print("----End----")
    return a


a1 = [1, 2, 3, 4, 5]
a2 = [5, 4, 3, 2, 1]
a3 = [1, 1, 1, 1, 1]
a4 = [1, 3, 2, 4, 5]
a5 = [5, 3, 1, 2, 4]
a6 = []
a7 = [1, 2, 3, 5, 4]

selection_sort(a1, show=True)
selection_sort(a2, show=True)
selection_sort(a3, show=True)
selection_sort(a4, show=True)
selection_sort(a5, show=True)
selection_sort(a6, show=True)
selection_sort(a7, show=True)

assert selection_sort(a1) == [1, 2, 3, 4, 5]
assert selection_sort(a2) == [1, 2, 3, 4, 5]
assert selection_sort(a3) == [1, 1, 1, 1, 1]
assert selection_sort(a4) == [1, 2, 3, 4, 5]
assert selection_sort(a5) == [1, 2, 3, 4, 5]
assert selection_sort(a6) == []
assert selection_sort(a7) == [1, 2, 3, 4, 5]

print("\nIf no AssertionError is raised then selection_sort is working as intended")