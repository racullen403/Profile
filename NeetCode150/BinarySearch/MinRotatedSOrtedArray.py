def findMinOfRotatedSortedArray(nums):
    l = 0 
    r = len(nums) - 1
    res = nums[0]
    while l <= r:
        if nums[l] < nums[r]:
            res = min(res, nums[l])
            break 
        m = (l + r) // 2
        res = min(res, nums[m])
        if nums[m] >= nums[l]:  # We are in the left sorted side and want to move to the right
            l = m + 1
        else:                   # We are in the right sorted side and want to move to the left
            r = m - 1
    return res

        
        
        




      
    return  nums[r + 1]
            


def test():
    n = [4,5,0,1,2,3]
    m = [3,4,5,6,1,2]
    print(findMinOfRotatedSortedArray(m))

test()