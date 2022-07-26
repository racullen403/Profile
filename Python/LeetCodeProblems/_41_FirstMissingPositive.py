"""
Given and unsorted integer array, nums, we must return the smallest missing positive number. Algorithm must O(n) and
use constant extra space.


Solution 1:

    - We know the largest possible missing positive number will be len(nums)+1

        e.g     [1, 2, 3, 4], 5 would be the first missing positive

    - Using this we can create an array of len(nums)+1

        positives = [ False for _ in range(len(nums)+1)]

    - We simply iterate through all of nums, if nums[i] < len(nums)+1 we update the index is positives to True to
    indicate that nums[i] is present.

    - Finally, we iterate through positives, the first time we come across False tells us that index (positive number)
    is missing, return this as the answer

    - Note, this solution return the correct answer, however, the extra space grows with length of the input, O(n)


Solution 2:

    - This is trickier, we store the information of existing positives, less than len(nums)+1, within the
    input array itself, this way we achieve O(1) extra space.

    - First preprocess the input array nums, if nums[i] <= 0 or nums[i] > len(nums), set nums[i] = 0

        e.g, [3, 4, -1, 1] -> [3, 4, 0, 1]

     - If nums[i] % (len(nums)+1) != 0, then the original number at nums[i] lies in 0<nums[i]<=len(nums),
     we can encode this into the input array using nums[i-1] += len(nums)+1. The use of % allows us to always get
     the original value in nums even if we +=len(nums)+1 .

        [3, 4, 0, 1] -> [8, 4, 5, 6]

    - Finally, we go through this new list, and do nums[i] // len(nums)+1, if we get 0, then the number represented
    by index i is missing, return i+1 (index 0 represent number 1, 1->2, 2->3 and so on). If we do not get a 0, then
    the first missing number is len(nums)+1


Solution 3:

    - We swap the numbers into their correct positions, iterating through nums.

    - Swaps occur while 0 < nums[i] <= len(nums) and nums[i] != nums[nums[i]-1]

        e.g     consider nums = [3, 4, -1, 1]


            i = 0

                nums -> [-1, 4, 3, 1]

                because nums[i] <= 0 we stop


            i = 1

                nums -> [-1, 1, 3, 4]
                     -> [1, -1, 3, 4]

                again, nums[i] <= 0  so stop


            i = 2

                nums[i] = nums[nums[i] - 1] so stop


            i = 3

                nums[i] = nums[nums[i] - 1] so stop

        - The final sorted array is nums = [1, -1, 3, 4], we now iterate through this until we find nums[i] != i+1,
        return i+1 or if all numbers match, return len(nums)+1

        - Note that everytime a swap is made, the number ends up in its correct position and will never be swapped
        again, as a result, in worst case we would make n-1 swaps, and then check through the remaining n terms once
        without performing any more swaps. As a result we get time complexity O(n) still, and space complexity O(1)
        as everything is done in place.

"""


def find_first_missing_positive_number(nums):
    positives = [False for _ in range(len(nums) + 1)]
    for i in range(len(nums)):
        if 0 < nums[i] <= len(nums):
            positives[nums[i] - 1] = True
    for i in range(len(positives)):
        if positives[i] is False:
            return i + 1


def find_fmp_hashing(nums):
    # Add 0 to end, allows for easier indexing
    nums.append(0)
    n = len(nums)
    # Preprocess array to remove useless numbers
    for i in range(n):
        if nums[i] < 0 or nums[i] >= n:
            nums[i] = 0
    # Record frequency of numbers, using the number (gives index) as a hash
    for i in range(n):
        nums[nums[i] % n] += n
    # Return first missing number with frequency 0
    for i in range(1, len(nums)):
        if nums[i] // n == 0:
            return i
    return n


def find_fmp_swapping(nums):
    n = len(nums)
    i = 0
    while i < n:
        if (0 < nums[i] <= n) and (nums[i] != nums[nums[i]-1]):
            temp = nums[nums[i]-1]
            nums[nums[i]-1] = nums[i]
            nums[i] = temp
        else:
            i += 1
    for i in range(n):
        if nums[i] != i+1:
            return i+1
    return n+1
