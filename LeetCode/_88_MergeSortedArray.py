"""
Given 2 increasing arrays, nums1 and nums2, where there are m integers in nums1 and n integers in nums2, and the length
of nums1 is m+n, sort the two arrays into nums1
"""


def merge_sorted_arrays(nums1, nums2, m, n):
    i = m + n - 1
    m -= 1
    n -= 1
    while m >= 0 and n >= 0:
        if nums1[m] >= nums2[n]:
            nums1[i] = nums1[m]
            m -= 1
        else:
            nums1[i] = nums2[n]
            n -= 1
        i -= 1
    while n >= 0:
        nums1[i] = nums2[n]
        n -= 1
        i -= 1
    return nums1


def test():
    nums1 = [1, 3, 5, 0, 0, 0]
    nums2 = [2, 4, 6]
    m = 3
    n = 3
    print(merge_sorted_arrays(nums1, nums2, m, n))


test()