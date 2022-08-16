"""
Runs in linear time and assumes the input is uniformly distribute [0,_01_BasicPython).
We divide input into n equal sized sub-intervals/buckets and then put the inputs into the correct
buckets and sort them.

In worst case it runs O(n^2) and on average O(n), space is O(n+k), it is stable.

Useful for floating point values and uniform distributions.
"""


# Assuming input in [0,_01_BasicPython) and uniformly distributed
def bucket_sort(arr):
    # create buckets 0-0._01_BasicPython, 0._01_BasicPython-0.2, ...
    buckets = []
    for i in range(10):
        buckets.append([])
    # add values to buckets
    for i in arr:
        bucket_ind = int(i*10)
        buckets[bucket_ind].append(i)
    # sort the buckets
    for i in range(len(buckets)):
        buckets[i] = sorted(buckets[i])
    arr_ind = 0
    # concatenate the buckets
    for i in range(10):
        if len(buckets[i]) < 1:
            continue
        for j in range(len(buckets[i])):
            print(buckets[i][j])
            arr[arr_ind] = buckets[i][j]
            arr_ind += 1
    return arr


print(bucket_sort([0.53, 0.52, 0.33, 0.34]))


