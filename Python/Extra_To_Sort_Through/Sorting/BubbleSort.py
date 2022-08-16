"""
Bubblesort:

    - Compare element on left to element on right, if larger, swap them
    - repeat until you reach end of array
    - do again on new array until no swaps occur, ie the array is sorted

Complexity:
    - I have added variables last_swap_ind and swapped, this adds space complexity
    O(2), we don't need them but they reduce processing. swapped lets us stop iterating
    once we don't do a swap. last_swap_ind keeps track of the position the most recent
    element was swapped to, this means on the next iteration we can stop comparing to
    the later elements since we know they are already sorted.
    - Time complexity, in best case array is sorted so O(n) after one compare loop. In
    the worst case we have descending order and have to loop for each element in the
    array, (n-_01_BasicPython)+(n-_01_BasicPython)+...+_01_BasicPython=n(n-_01_BasicPython)/2 ~ O(n^2)
"""


# Think of bubble sort as "bubbling" the largest term to the last position on each iteration
def bubble_sort(a, show=False):
    if show is True:
        print("\n----Bubble Sort----")
        print("Starting array: " + str(a))
    # index of last position an element was swapped to
    last_swap_ind = len(a) - 1
    # iterate and break when a swap doesn't occur
    for i in range(len(a)):
        if show is True:
            print("LOOP " + str(i+1) + ":" + str(a))
        swapped = False
        swap_ind = 0
        # iterate over elements up to the last sorted position
        for j in range(0, last_swap_ind):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                swapped = True
                last_swap_ind = j
                swap_ind += 1
                if show is True:
                    print("  SWAP " + str(swap_ind) + ": " + str(a))
        if swapped is False:
            break
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

bubble_sort(a1, show=True)
bubble_sort(a2, show=True)
bubble_sort(a3, show=True)
bubble_sort(a4, show=True)
bubble_sort(a5, show=True)
bubble_sort(a6, show=True)


assert bubble_sort(a1) == [1, 2, 3, 4, 5]
assert bubble_sort(a2) == [1, 2, 3, 4, 5]
assert bubble_sort(a3) == [1, 1, 1, 1, 1]
assert bubble_sort(a4) == [1, 2, 3, 4, 5]
assert bubble_sort(a5) == [1, 2, 3, 4, 5]
assert bubble_sort(a6) == []

print("\nIf no AssertionError is raised then bubble_sort is working as intended")