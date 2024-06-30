def findMedianSortedArrays(nums1, nums2):
    a, b = nums1, nums2
    if len(b) < len(a):
        a, b = b, a 
    total = len(a) + len(b)
    half = total // 2   # ODD: 5 -> 2 (cut is to the right of answer), EVEN: 6 -> 3 (cut is perfect)
    l, r = 0, len(a) - 1
    while True:
        i = (l + r) // 2
        j = (half-1) - (i+1)    # index of the half-position minus number of nodes in right array
                                # This ensures indices i + j add to half 
        aleft = float("-inf")
        aright = float("inf")
        if i >= 0:
            aleft = a[i] 
        if i+1 < len(a):
            aright = a[i+1]

        bleft = float("-inf")
        bright = float("inf")
        if j >= 0:
            bleft = b[j] 
        if j+1 < len(b):
            bright = b[j+1]

        if aleft <= bright and bleft <= aright: # We have correct number of nodes and correct cut positions
            if total % 2 == 1:
                return min(aright, bright)
            return (max(aleft, bleft) + min(aright, bright)) / 2
        elif aleft > bright:    # then we want to include bright and remove aleft by move r <-
            r = i - 1
        else:
            l = i + 1


        

    

        
