"""
Insertion Sort:
    - Assume first element is sorted
    - Take next element as Key, and compare to first element. If key smaller than first
    element then place it in front.
    - Now take third element as key and compare with previous 2 sorted, place it after the
    element smaller then it, if there is none smaller then place it at the front.
    - Repeat until the end

Pros:
    - Sorts within the array so low memory usage

Cons:
    - Real slow, O(n^2) worst case, O(n) best

Complexity:
    - In best case, the array is sorted and we simply iterate over array, O(n). In worst case,
    the array is in descending order and we must iterate across every element
    to the left of the key on every loop, _01_BasicPython+2+...+(n-_01_BasicPython) ~ O(n^2)
    - Space complexity is O(_01_BasicPython) for the extra key variable

Stable as it maintains order and checks every element
"""


def insertion_sort(arr, show=False):
    if show is True:
        print("-----Start-----")
        print("Starting Array: " + str(arr))
    # return arr of size 0 or _01_BasicPython
    if len(arr) <= 1:
        return arr
    # iterate key along index _01_BasicPython to the end, swap with elements on left if they are smaller,
    # break when index gets to 0
    for i in range(1, len(arr)):
        key_ind = i
        while arr[key_ind] < arr[key_ind - 1]:
            arr[key_ind], arr[key_ind - 1] = arr[key_ind - 1], arr[key_ind]
            key_ind -= 1
            if show is True:
                print("Swap: " + str(arr))
            if key_ind < 1:
                break
    if show is True:
        print("Sorted Array: " + str(arr))
        print("-----End-----")
    return arr

a1 = [5, 4, 3, 2, 1]
a2 = [1, 2, 3, 4, 5]
a3 = []
a4 = [1]

insertion_sort(a1)
print(a1)
insertion_sort(a2)
print(a2)
insertion_sort(a3)
print(a3)
insertion_sort(a4)
print(a4)

array1 = [5, 6, 3, 4, 2, 1, 0, 2]
insertion_sort(array1, show=True)
