def productExceptSelf(nums):
    # Medium: given position i, we want to know the product from 0 up to 
    # i-1 and then muliply this by the product from end back to i+1.
    # We can do this creating a prefix and suffix array in each case.
    pre = [1] * len(nums)
    suf = [1] * len(nums)
    for i in range(len(nums)):
        if i == 0:
            pre[i] = nums[i]
        else:
            pre[i] = pre[i-1] * nums[i] 
    for i in range(len(nums)-1, -1, -1):
        if i == len(nums) - 1:
            suf[i] = nums[i]
        else:
            suf[i] = suf[i + 1] * nums[i]
    res = [0] * len(nums) 
    for i in range(len(nums)):
        if i == 0:
            res[0] = suf[1]
        elif i == len(nums) - 1:
            res[i] = pre[i-1]
        else:
            res[i] = pre[i-1] * suf[i+1]
    return res

def cleanerImplementation(nums):
    res = [1] * len(nums)
    for i in range(1, len(nums)):
        res[i] = res[i-1] * nums[i-1]   # Creates the prefix array
    suf = 1 # initials suffix array(we actually only need 1 variable)
    for i in range(len(nums)-1, -1, -1):
        res[i] *= suf   # simply multiply prefix array by suffix value
        suf *= nums[i]  # then increase suffix value
    return res
    

def example():
    a = [-1,0,1,2,3]
    cleanerImplementation(a)

example()
    
    