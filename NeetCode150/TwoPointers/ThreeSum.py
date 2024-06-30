def threeSum(nums):
    # Medium: assume target is 0. Same situation as twoSum but with 
    # extra step, increasing complexitiy to O(n^2) therefore we sort 
    # array first in (nlogn)
    nums.sort()
    res = [] 
    for i in range(len(nums)):
        if nums[i] > 0:
            break 
        if i > 0 and nums[i] == nums[i-1]:
            continue
        l = i + 1
        r = len(nums) - 1
        while l < r: 
            total = nums[i] + nums[l] + nums[r] 
            if total == 0:
                res.append([nums[i], nums[l], nums[r]])
                while l < r and nums[l] == nums[l + 1]:
                    l += 1
                r -= 1
                l += 1
            elif total < 0:
                l += 1
            else: r -= 1
    return res
