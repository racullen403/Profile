"""
Given an array of n non-negative integers, representing and elevation map of bars with width 1, compute how much
water can be trapped after raining.


Solution:

   - We simply use a contracting window to find the amount of water that can be stored at a given index.

   - We want to keep track of the current maximum height the water can be at, min(walls[l], walls[r]), and the outer
   walls, walls[l] and walls[r]. If the maximum height ever increases, we add the new "extra" potential volume of
   water to the total and nore this new max height.

   - Once the initial height change has been checked, we remove the height of the smaller wall from the total and
   move the pointer inwards. In this way, we pre-calculate the total area including the walls, and then move our
   pointers inwards, removing the heights of the walls until a new water depth is found, this new potential area is
   added to the total, and we continue as before


"""


def trapped_water(walls):
    l, r = 0, len(walls)-1
    max_height = 0
    total = 0
    while l < r:
        height = min(walls[l], walls[r])
        if height > max_height:
            total += (height-max_height)*(r-l+1)
            max_height = height
        if walls[l] <= walls[r]:
            total -= min(max_height, walls[l])
            l += 1
        else:
            total -= walls[r]
            r -= 1
    total -= max_height
    return total






