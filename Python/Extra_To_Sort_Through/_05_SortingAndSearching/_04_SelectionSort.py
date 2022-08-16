"""
Selection Sort improves on Bubble Sort by only making 1 exchange on each pass through
the list. It does this by finding the largest item in the list of size n, and then swapping
it with the final nth position. We then consider the list of length n-1 and do the same,
repeating until we have 1 item left to sort.

Selection Sort still runs in O(n^2) time, however it uses less swaps then bubble sort and performs
better
"""


def selection_sort(alist):
    for i in range(len(alist)):
        largest_index = 0
        for j in range(len(alist)-i):
            if alist[j] > alist[largest_index]:
                largest_index = j
        alist[largest_index], alist[len(alist)-i-1] = alist[len(alist)-i-1], alist[largest_index]
    return alist

print(selection_sort([5,3,2,4,1]))