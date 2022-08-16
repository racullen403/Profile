"""
Counting Sort:
    - Sorts elements in an array by number of occurrences, storing count in auxiliary array, and
    mapping the count as an index.
    - Find max element, create count array 0-max, store count of each element at its index,
    eg 5 -> 5th index
    - Convert count array to cumulative count
    - Use count array to find correct index in original array, decrease count by _01_BasicPython
    - Repeat for all elements in the original array

Complexity:
    - Our loops run both over the entire array a O(n) and over the count array O(k) so overall
    time complexity is given by O(n+k)
    - Space complexity is dependent on the the range of values, ie count array will change size
    - Note that count sort is not a comparative sorting algorithm so no lower bound of nlogn

Stable: numbers with the same value appear in the output array in the same order as they do in
the input array
"""


def count_sort(arr):
    if len(arr) <= 1:
        return arr
    # Find largest +ve integer
    largest = arr[0]
    for i in arr:
        if i > largest:
            largest = i
    # Create storage and output arrays
    storage = [0]*(largest+1)
    output = [0]*len(arr)
    # Count inputs
    for i in arr:
        storage[i] += 1
    # Create Cumulative counts
    for i in range(0, len(storage)-1):
        storage[i+1] += storage[i]
    # Insert integers into correct position in output, reverse order to ensure stability
    for i in range(len(arr)-1, -1, -1):
        storage[arr[i]] -= 1
        output[storage[arr[i]]] = arr[i]
    return output

print("----Count Sort----")
a = [5, 5, 4, 2, 0, 1, 1, 3]
print(a)
print(count_sort(a))


# Count sort to include negatives
def count_sort_negatives(arr, show=False):
    if len(arr) <= 1:
        return arr
    # Find Max and Min, this way we know if negatives exist and can use special logic
    max = arr[0]
    min = arr[0]
    for i in range(len(arr)):
        if arr[i] > max:
            max = arr[i]
        if arr[i] < min:
            min = arr[i]
    # Set max value
    if abs(min) > abs(max):
        max = abs(min)
    else:
        max = abs(max)
    # Initialise arrays
    storage = [0]*(2*max+1)
    output = [0]*len(arr)
    # Calc the number of positive values if negatives exist
    positive_count = 0
    if min < 0:
        for i in range(len(arr)):
            if arr[i] >= 0:
                positive_count += 1
    negative_count = len(arr) - positive_count
    # Count
    for i in arr:
        storage[i] += 1
    # Cumulative count
    for i in range(len(storage)-1):
        storage[i+1] += storage[i]
    if show is True:
        print("Starting: " + str(arr))
        print("Max: " + str(max))
        print("Min: " + str(min))
        print("Count: " + str(storage))
        print("Cumulative: " + str(storage))
        print("Positive Count: : " + str(positive_count))
        print("Negative Count: : " + str(negative_count))
    # Create sorted array, if negatives exist we shift positive values up and negatives
    # down from the end, reverse order to ensure stability
    for j in range(len(a)-1, -1, -1):
        if arr[j] >= 0 and min < 0:
            ind = storage[arr[j]]-1 + negative_count
        elif arr[j] < 0 and min < 0:
            ind = storage[arr[j]]-1 - positive_count
        else:
            ind = storage[arr[j]]-1
        output[ind] = arr[j]
        storage[arr[j]] -= 1
        if show is True:
            print("Array " + str(j) + ": " + str(output))
    return output


print("----Count Sort with Negatives----")
a = [5, -5, 4, -2, 0, 1, 1, 3]
count_sort_negatives(a, True)
