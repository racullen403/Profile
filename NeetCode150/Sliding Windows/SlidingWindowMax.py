def maxSlidingWindow(nums, k):
    # Hard: We need to keep track of the nums in descending order for given window, best done with a deque 
    # but can be implemented with an array and pointer for left most position of the largest value. Simply 
    # track largest values from left to right, poping smaller values out of queue if needed. If the pop 
    # results in our largest value in the current window being popped, then decrease q pointer. Append new 
    # smallest value to queue, and adjust q pointer as needed (new value may actually be the new largest).
    if len(nums) < k:
        return 
    res = [] 
    l = 0 
    r = 0
    ql = 0
    q = [] 
    while r < len(nums): 
        while q and nums[r] >= nums[q[-1]]:
            if ql != 0 and q[ql] == q[-1]:
                ql -= 1
            q.pop()
        q.append(r)
        if q[ql] < l:
            ql += 1
        if r + 1 >= k:
            res.append(nums[q[ql]])
            l += 1
        r += 1
    return res
            
        