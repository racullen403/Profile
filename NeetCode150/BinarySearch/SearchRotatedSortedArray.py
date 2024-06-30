def findTargetOfRotatedSortedArray(nums, target):
    l = 0 
    r = len(nums) - 1
    while l <= r:
        m = (l + r)//2
        if nums[m] == target:
            return m 
        elif nums[m] > nums[r]:
            if target > nums[m] or target < nums[l]:
                l = m + 1
            else:
                r = m - 1
        else:
            if target > nums[m] or target < nums[l]:
                l = m + 1
            else:
                r = m - 1
    return -1
