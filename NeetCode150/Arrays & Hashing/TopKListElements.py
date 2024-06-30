def topKFrequent(nums, k):
    # Medium: Create a list of lists where index indicates the total count.
    # Calculate the total counts of nums
    # Iterate through adding them to respective counts list
    # Return the final k nums
    # O(n)
    counts_list = [[] for _ in range(len(nums) + 1)]
    lookup = {}
    for i in range(len(nums)):
        lookup[nums[i]] = 1 + lookup.get(nums[i], 0)
    for num, count in lookup.items():
        counts_list[count].append(num)
    output = []
    total = 0
    for i in range(len(counts_list)-1, -1, -1):
        for num in counts_list[i]:
            output.append(num)
            total += 1
            if total == k:
                return output