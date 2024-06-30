def longestConsecutive(nums):
    # Medium: we add all numbers to a set. Then iterate through until
    # we find a number that has no number to its left. From here, count
    # the sequence until it ends.
    lookup = set()
    for num in nums:
        lookup.add(num)
    longest = 0
    for num in lookup:
        if num - 1 in lookup:
            continue
        else:
            count = 1
            while num + 1 in lookup:
                count += 1
                num += 1
            longest = max(longest, count)
    return longest