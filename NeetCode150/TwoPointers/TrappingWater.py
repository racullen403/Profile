def trap(height):
    # Hard: My approach, find total area between all heights, 
    # moving up in height levels, 
    # then subtract the heights to find the gaps between.
    l = 0
    r = len(height) - 1
    h = 1
    area = 0
    while l <= r:
        while l < r and height[l] < h:
            l += 1
        while l < r and height[r] < h:
            r -= 1
        if l == r:
            area += height[l] - h + 1
            break
        area += (r - l + 1)
        h += 1
    for num in height:
        area -= num 
    return area


def trap2(height):
    # Hard: We keep track of l and r points for both left and right positions
    # as well as lmax and rmax pointers for the largest left and right heights 
    # from l and r. We can then calculate based on smallest max height, if the 
    # l/r new pointer position can contain trapped water and whether we need to update 
    # max heights.
    l = 0
    r = len(height) - 1
    lmax = height[0]
    rmax = height[-1]
    area = 0
    while l < r:
        if lmax <= rmax:
            area += max(lmax - height[l], 0)
            l += 1
            lmax = max(lmax, height[l])
        else:
            area += max(rmax - height[r], 0)
            r -= 1
            rmax = max(rmax, height[r])
    return area
        
        




        

