"""
Bucket Sort:

    This method divides objects up into relative buckets/groupings. These unsorted buckets are then sorted using a
    suitable sorting algorithm or recursively applying bucket sort again. We then combine the buckets to form the
    final array.

    This method is very dependent on the distribution of the input array, to ensure the objects get spread over the
    buckets.


Time Complexity:
    - When most objects are placed into the same bucket, our complexity is now dependent on the sorting method used.
    - The best case occurs when objects are uniformly distributed
    Creation of the buckets is O(n)

Space Complexity:
    This will simply be O(n) to create a copy of the input array, spread over the buckets, we would then also need to
    consider the sorting method used.

Note that placing into the buckets retains Stability.

This method is useful for floating point numbers
"""


# Example, incomplete
def bucket_sort(array):
    bucket = []
    for i in range(len(array)):  # create buckets
        bucket.append([])
    for j in array:  # sort objects into buckets
        index_b = ...
        bucket[index_b].append(j)
    for i in range(len(array)):  # apply sorting algo on each bucket
        bucket[i] = "sort method"
    # Get the sorted elements
    k = 0
    for i in range(len(bucket)):  # combine buckets
        for j in range(len(bucket[i])):
            array[k] = bucket[i][j]
            k += 1
    return array