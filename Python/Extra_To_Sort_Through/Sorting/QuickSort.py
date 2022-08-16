"""
Quick Sort:
    - Divide and conquer
    - Choose pivot element (far right), elements smaller than pivot are placed to the left,
    elements greater are placed to the right.
    - Repeat this for the left sub array and right sub array until they are a single element,
    at this point they are sorted

In worst case it is O(n^2) but on average it is O(nlogn) (even with 9-_01_BasicPython split), it is very
practical and sorts the array in place, so low memory usage.

Unstable
"""


def quick_sort(arr, l, r):
    if l < r:
        pivot = partition(arr, l, r)
        quick_sort(arr, l, pivot-1)
        quick_sort(arr, pivot+1, r)
    return


def partition(arr, l, r):
    i = l
    j = l
    while j < r:
        if arr[j] <= arr[r]:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1
            j += 1
        else:
            j += 1
    arr[r], arr[i] = arr[i], arr[r]
    return i

print("----Quick Sort _01_BasicPython----")
a = [4, 3, 1,  5, 0, 7, 2]
print(a)
quick_sort(a, 0, len(a)-1)
print(a)


print("----Quick Sort 2----")
a = [5, 3, 2, 5, 2, 3, 0]
print(a)
quick_sort(a, 0, len(a)-1)
print(a)

