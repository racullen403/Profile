"""
We must create an algorithm for finding the largest container of water
in a list of heights.

    heights = [4, 2, 1, 1, 5, 9, 3]

    We assume each index represents a wall of height stated, and that the walls are
    all separated by  unit distance.

    We want to know what 2 walls can contain the most water in them.


Solution:
    Let l and r be pointers for the current walls, then the current area of water contained will be

        area = (r-l)*min(heights[l], heights[r])

    If we start with l = 0 and r=len(heights)-1, ie the largest base possible, then by shrinking this base,
    the only way the area can possibly increase is if we were to increase the heights of the walls. This is key
    so solving this in O(n) time.

    - We simply find the initial area of water contained, then look at the heights of the walls of l and r

        - if heights[l] <= heights[r], we move l to the right until we find a new wall that is larger than the
        original l, as this has the potential to have a new larger area.
        - else more r to the left until we find a new larger wall than the original r.
        - ensure l < r always otherwise we are done
"""


def max_container_water(heights):
    l = 0
    r = len(heights)-1
    i = l
    j = r
    while l < r:
        area = min(heights[l], heights[r]) * (r-l)
        if area > min(heights[i], heights[j]) * (j-i):
            i = l
            j = r
        if heights[l] <= heights[r]:
            start = l
            while l < r and heights[l] <= heights[start]:
                l += 1
        else:
            start = r
            while l < r and heights[r] <= heights[start]:
                r -= 1
    return i, j
