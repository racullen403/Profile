"""
Medium: Given unsorted array of integers, return the kth largest.

Sol:
    - Create max heap and pop with first k-1 terms, new top position is the kth largest. This will be O(klogn).

    - Sort in nlogn and choose kth value.

    - We can use Quick Select algorithm, similar to Quick Sort, to get an average case of O(n) and worst case O(n^2)
        - We use the pivot method to partition the array, we can then tell which part of the array the target value is in.
        - Once our pivot finishes in the kth place, we have our result.
"""

import heapq 

def findKthLargest(nums, k):    # minHeap O(klogn)
    nums = [-n for n in nums]
    heapq.heapify(nums)
    for _ in range(k-1):
        heapq.heappop(nums)
    return -1 * nums[0]


def kthLargest(nums, k):
    k = len(nums) - k 

    def quickSelect(l, r):
        pivot = nums[r] 
        i = l 
        for j in range(l, r):
            if nums[j] <= pivot:
                nums[j], nums[i] = nums[i], nums[j]
                i += 1
        nums[i], nums[r] = nums[r], nums[i]
        if i < k:
            return quickSelect(i + 1, r)
        elif i > k:
            return quickSelect(l, i - 1)
        else:
            return nums[i]
    
    return quickSelect(0, len(nums) - 1)
