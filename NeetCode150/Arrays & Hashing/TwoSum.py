def twoSum(nums, target):
    # Easy: add nums to lookup with index, for each num try to find if
    # target - num exists. O(n) time and memory
    lookup = {}
    for i in range(len(nums)):
        find = target - nums[i]
        if find in lookup and lookup[find] != i:
            return lookup[find], i
        lookup[nums[i]] = i 
