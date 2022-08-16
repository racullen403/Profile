"""
Has the same runtime of mergesort, O(nlogn) but sorts heap in place, meaning efficient memory
usage.

We simply build a heap from the array by applying Heapify from the last internal node (n-_01_BasicPython)//2
back to the root. We then swap the root with the last leaf, decrease the size by _01_BasicPython, and heapify.
Repeat this process until size is 0.

Building the head takes O(n)
Sorting takes O(nlogn)
Space O(_01_BasicPython)
Not Stable
"""


# heapify for max heap property, compare parent and children, swap if necessary and heapify the
# swapped index
def heapify(arr, i, n):
    largest = i
    l = (2*i) + 1
    r = (2*i) + 2

    if l < n and arr[largest] < arr[l]:
        largest = l
    if r < n and arr[largest] < arr[r]:
        largest = r
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, largest, n)


# Build Max heap from an arr
def max_heap(arr):
    for i in range((len(arr)//2) - 1, -1, -1):
        heapify(arr, i, len(arr))


# heap sort on an array
def heap_sort(arr):
    n = len(arr)
    max_heap(arr)
    for i in range(n-1, 0, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, 0, i)




print("----Build Max Heap-----")
a1 = [4, 3, 2, 8, 5, 2, 10, 1, 23]
max_heap(a1)
print(a1)

print("\n----Heap Sort a=[4, 3, 2, 8, 5, 2, 10, _01_BasicPython, 23]-----")
a = [4, 3, 2, 8, 5, 2, 10, 1, 23]
heap_sort(a)
print(a)