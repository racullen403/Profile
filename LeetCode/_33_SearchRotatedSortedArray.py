"""
We are given an integer array of sorted numbers (ascending and distinct), nums. Nums may have also been rotated at some
unknown pivot index k,

    e.g         [nums[0], ..., nums[k-1], nums[k], ..., nums[n-1]]

        ->      [nums[k], ..., nums[n-1], nums[0], ..., nums[k-1]]

Given nums after a possible unknown rotation, and a target integer tar, return the index of tar if it exists, or -1 if
it is not in nums, we must find this in O(logn) time complexity.


Solution 1:

    - First we need to find the pivot index in O(logn), we can do this with a binary search method:

        - The pivot exists if nums[0] > nums[-1], since the array started in increasing order before rotation.
        - Let l=0, r=len(nums)-1, and mid=(l+r)//2.
        - We do a binary search, moving l to mid if nums[mid] > nums[l] and r to mid otherwise. This will end in
        the following situation:

            [nums[k], ...., nums[n-1], nums[0], ... nums[k-1]]
                                  |
                                 l=r    pivot found!

        - Set the pivot=l+1 (note if we determined there is no pivot, skip previous).
        - Now all we need to determine is what interval our target value should lie in and then do a binary
        search for it in that interval


Solution 2:

    - This solution is more concise than the previous but requires more comparisons at each mid-point.

    - We calc mid=(l+r)//2 as before and determine which interval mid lies in, if nums[l] <= nums[mid], then mid is
    in the "left" interval, if nums[l] > nums[mid], then mid would be in the "right" interval.

        e.g     [4, 5, 6, 0, 1, 2]      "left" [4, 5, 6], "right" [0, 1, 2]

                [0, 1, 2, 3]            this whole array is the "left" interval

    - If mid is in left interval, we now need to determine where the target value lies:
        - If nums[l] <= tar < nums[mid], target lies from l-mid, then we move down r=mid-1, else target lies in mid-r
        so l moves up l=mid+1

    - If mid is in the right interval, we again determine where the target lies:
        - If nums[mid] < tar <= nums[r] then l=mid+1 else r=mid-1
"""


# Solution 1, more broken down and easier to understand
def search_rotated_array(nums, tar):
    l, r, i, j = 0, len(nums)-1, 0, len(nums)-1
    # If pivot exists, find it and correct interval target lies in
    if nums[l] > nums[r]:
        while l < r:
            mid = (l+r)//2
            if nums[mid] > nums[l]:
                l = mid
            else:
                r = mid
        pivot = l+1
        # Find the correct interval to search in
        if tar < nums[0]:
            i = pivot
            j = len(nums)-1
        else:
            i = 0
            j = pivot-1
    # Binary Search the correct interval for target
    while i < j:
        mid = (i+j)//2
        if nums[mid] < tar:
            i = mid+1
        else:
            j = mid
    if nums[i] == tar:
        return i
    return -1


# Solution 2, more complicated but concise
def search_rotated_array_2(nums, tar):
    l, r = 0, len(nums)-1
    while l <= r:
        mid = (l+r)//2
        if nums[mid] == tar:
            return mid
        if nums[l] <= nums[mid]:
            if nums[l] <= tar < nums[mid]:
                r = mid-1
            else:
                l = mid+1
        else:
            if nums[mid] < tar <= nums[r]:
                l = mid+1
            else:
                r = mid-1
    return -1

