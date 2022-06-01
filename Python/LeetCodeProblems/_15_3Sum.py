"""
We are given a list of numbers and have to find unique triplets that add to
0.

Solution 1:
    - We can solve this by splitting all the numbers into 3 lists,
    positives, negatives and zeros.
    - We check for 3 or more zeros and add (0,0,0)
    - If there is at least 1 zero, we go through unique positive list and check
    for the negative, adding (x, 0, -x)
    - We then take pairs of positive numbers and search for their complement
    in the negative set
    - Do the same but starting with pairs of negatives and finding a positive
    - We also keep a set of each of the positive and negative terms for O(1) lookup
    - Still O(n^2) solution, but very efficient.
"""


def three_sum_lists_solution(numbers):
    p, n, z = [], [], []
    for num in numbers:
        if num > 0:
            p.append(num)
        elif num < 0:
            n.append(num)
        else:
            z.append(num)
    # We now have our 3 lists
    P, N = set(p), set(n)
    # P and N are sets of unique nums for O(1) lookup
    output = set()
    # Case 1, 3 or more zeros
    if len(z) >= 3:
        output.add((0, 0, 0))
    # Case 2, 1 or more zeros
    if len(z) >= 1:
        for i in P:
            if -i in N:
                output.add((i, 0, -i))
    # Case 3, for each negative pair find the positive term
    for i in range(len(n)):
        for j in range(i+1, len(n)):
            target = -(n[i] + n[j])
            if target in P:
                output.add(tuple(sorted([n[i], n[j], target])))
    # Case 4, for each positive pair find the negative term
    for i in range(len(p)):
        for j in range(i+1, len(p)):
            target = -(p[i] + p[j])
            if target in N:
                output.add(tuple(sorted([p[i], p[j], target])))
    return output

""" 
Solution 2:
    - We can sort the initial list and iterate through it with 3 pointers 
    - The first pointer iterates left to right giving us the index of our 
    first number
    - We then have a left, l, and right, r, pointer. r starts furthest right 
    and l starts 1 position to the right of our index pointer.
    - if our total < 0, then move l right, if total > 0, move r left, else add the numbers to the output
    - Continue while l < r, then move index pointer 1 position right and 
    start again.
    - Do this until the index pointer is at a positive number or len(nums)-2 and stop.
    - This should run in O(n^2) time
"""


def three_sum_pointer_solution(nums):
    if len(nums) < 3:
        return None
    nums.sort()
    output = set()
    for i in range(len(nums) - 2):
        if nums[i] > 0:
            break
        l = i + 1
        r = len(nums) - 1
        while l < r:
            total = nums[i] + nums[l] + nums[r]
            if total == 0:
                output.add((nums[i], nums[l], nums[r]))
                while l < r and nums[l] == nums[l + 1]:
                    l += 1
                while l < r and nums[r] == nums[r - 1]:
                    r -= 1
                l += 1
                r -= 1
            elif total > 0:
                r -= 1
            else:
                l += 1
    return output
