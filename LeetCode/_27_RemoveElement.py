"""
We are asked to remove every instance of element with value "val" in an array, in-place. (See _26_)

Solution:
    - Simply use a pointer for the position we are placing an element into and iterate through the list.
    - If the element is not "val", then place it at "pos" and move "pos" forward once.
    - We return the new list with the index of the last position, i.e. nums[0:pos+1] will be the list the has "val"
    removed.
"""


def remove_val(nums, val):
    pos = 0
    for i in range(len(nums)):
        if nums[i] != val:
            nums[pos] = nums[i]
            pos += 1
    return nums, pos


print(remove_val([1,1,3,1,2], 1))
