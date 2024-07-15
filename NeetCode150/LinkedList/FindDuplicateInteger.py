def findDuplicate(nums):
    """
    Medium: Given an array of integers, nums, length n+1 where integers range inclusive [1, n] (ie alway duplicate). 
    Every integer appears once except for one which will appear two or more times. Return the integer that appears more than once, 
    without modifying nums and using O(1) space.

    Sol:
        - If we treat the integers as pointer for an equivalent linked list, because there is a duplicate, there will be a cycle.
        - We can apply our fast and slow pointer method like in CycleDetection to find the a point in this cycle (intersection).
        - We then apply Floyd's Algorithm, the distance from the start of list to first cycle position is the same as distance from the intersection to the 
        starting point of cycle

        At point of intersection

            - slow pointer moves distance P + s*C - X       (P is distance to cycle, C is cycle length X is distance from poisiton in cycle to start/end)
            - fast pointer moves distance P + f*C - X
            - we know 2*slow = fast

                2P + 2sC - 2X = P + fC - X 
                P = X - nC where n is some integer

                therfore distance P to cycle is the same as distance X of intersection to start of cycle

        - Hence by move from start and intersection, one position at a time, they will be equal at the start of the cycle, the first duplicate number.


    """
    # Find intersection
    fast, slow = 0, 0
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]
        if slow == fast:
            break
    
    # Use Floyds to find start of cycle
    slow2 = 0
    while True:
        slow = nums[slow]
        slow2 = nums[slow2]
        if slow == slow2:
            return slow

        
