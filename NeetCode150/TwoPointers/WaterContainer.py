def maxArea(heights):
    # Medium: given array of heights, find max area of water 
    # that can be stored.
    res = 0 
    l = 0
    r = len(heights) - 1
    while l < r:
        area = (r - l) * min(heights[l], heights[r])
        res = max(res, area)
        if heights[l] < heights[r]:
            l += 1
        else:
            r -= 1
    return res