"""
Given an array on integer numbers, sort it into ascending order and return it. Must solve in O(nlogn) time, and
with O(1) space complexity.


Solution:
    - We know Mergesort is a logarithmic sorting method that can be used, however, the recursion tree causes an
    O(nlogn) space complexity as we must pass down "chunks" of the array inorder to use them to sort the input array.
    - Another option is the Quicksort method, this runs in O(nlogn) time. In this case, we can do all the sorting
    in-place within the original array, all that would need to be passed down into the recursion tree would be the
    indices of the "chunk" we are at. Note that quicksort has a worst case O(n^2) time complexity, as a result we
    would apply randomisation (randomised QuickSelect) to the pivot to achieve an expected O(nlogn) or we use
    median of medians method to find the pivots and achieve worst case O(nlogn).

"""


def sort_array(nums):

    def partition(l, r):
        swap = l
        for i in range(l, r):
            if nums[i] <= nums[r]:
                nums[i], nums[swap] = nums[swap], nums[i]
                swap += 1
        nums[r], nums[swap] = nums[swap], nums[r]
        return swap

    def quick_sort(l, r):
        if l < r:
            p = partition(l, r)
            quick_sort(l, p-1)
            quick_sort(p+1, r)

    quick_sort(0, len(nums)-1)

    return nums


def example():
    arr = [9, 4, 3, 8, 6, 5]
    print("Initial Arr:", arr)
    sort_array(arr)
    print("Sorted Arr:", arr)


