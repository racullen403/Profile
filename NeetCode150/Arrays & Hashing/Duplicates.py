def hasDuplicate(nums):
    # Easy: use set to find dups in O(1)
    lookup = set()
    for num in nums:
        if num in lookup:
            return True
        lookup.add(num)
    return False