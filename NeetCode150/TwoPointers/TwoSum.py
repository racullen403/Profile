def twoSum(numbers, target):
    # Medium: note array is in increasing order and always one solution
    # makes easier as we dont need to use hashmap to find values. 
    l = 0 
    r = len(numbers) - 1
    while l < r:
        total = numbers[l] + numbers[r]
        if total == target:
            return l, r 
        elif total > target:
            r -= 1
        else:
            l += 1

def twoSumNotSorted(nums, target):
    lookup = {}
    for i in range(len(nums)):
        find = target - nums[i] 
        if find in lookup:
            return lookup[find], i
        lookup[nums[i]] = i 
    return -1, -1
