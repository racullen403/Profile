"""
A version of Insertion sort that sorts elements in an interval some distance apart, and then
reduces the distance and compares elements in this new interval, continuing until the distance is
_01_BasicPython and we compare elements side by side.

The sequence we use for interval can change, and is optimal depending on the input, we will look
at Shell's sequence N/2, N/4, N/8, ..., _01_BasicPython

Working:
    - Compare elements at position 0 and N/2, swap if necessary
    - Move now to _01_BasicPython and _01_BasicPython+N/2 and compare, continue until end of array.
    - Change distance to N/4, repeat process, however, we need to consider all elements in the
    interval, so at some point we get to 0 N/4 N/2, which moves up until 0 N/4 N/2 3N/4
    - Proceed like this until sequence is _01_BasicPython and we compare elements side by side, eg 0 _01_BasicPython, then
    0 _01_BasicPython 2, then 0 _01_BasicPython 2 3, ..., 0 _01_BasicPython 2 ... n and done.

Run time is on average O(nlogn) and worst case O(n^2)
"""


def shell_sort(arr):
    print("\n----Shell Sort----")
    print("  Starting Array: ", arr)
    n = len(arr)
    interval = n // 2
    while interval > 0:
        print("Interval: ", interval)
        for i in range(interval, n):
            j = i
            print(" Checking ind: ", i)
            # compare the ith position with on interval behind it, then, the interval behind with the
            # interval behind that and so on until until j is smaller than the interval, in which case
            # another interval behind would bring us out of the index range.
            while j >= interval and arr[j - interval] > arr[j]:
                arr[j], arr[j-interval] = arr[j-interval], arr[j]
                print("  Swap ind {} with {}: ".format(j, j-interval) + str(arr))
                j -= interval
        interval = interval // 2
    print("\nSorted Array: ", arr)
    return arr

shell_sort([2, 3, 5, 2, 5, 2, 3, 5, 7, 8, 9, 8])
shell_sort([9, 8, 3, 7, 5, 6, 4, 1])