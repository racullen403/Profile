"""
Radix sort:

    - Sorts by first grouping the individual digits of the same place value and then
    sorting elements in order. eg group by unit digit and sort, then group by tenth digit
    then sort, then hundredth digit and sort...
    - Start by finding Max value and calculating the number of digits in it, X.
    - Go through each significant place and apply a "Stable" sorting technique

Complexity:

    - Time O(a(n+k)), non comparative, faster than O(nlogn)
    - Space O(max), very space inefficient especially with large number, this is why it isnt
    used in software libraries

Stable
"""


def radix_sort(arr):
    print("\n----Radix Sort----")
    print("Starting Array: " + str(arr))
    # find largest value
    max = arr[0]
    for i in arr:
        if i > max:
            max = i
    print("Max: " + str(max))
    # find number of digits
    digits = 0
    while max > 0:
        digits += 1
        max = max//10
    print("Digits: " + str(digits))
    # apply digit count sort on the 1st digit, then 2nd, then 3rd...
    for d in range(1, digits+1):
        arr = count_sort_digits(arr, d)
        print("Sort Digit {}:".format(d) + str(arr))
    print("----Sorted----")
    return arr


def count_sort_digits(arr, digit):
    # create count and sorted arrays
    count = [0]*10
    sorted = [0]*len(arr)
    # add counts to count
    for i in range(len(arr)):
        count_ind = (arr[i] // 10**(digit-1)) % 10
        count[count_ind] += 1
    # convert to cumulative count
    for i in range(len(count)-1):
        count[i+1] += count[i]
    # place arr values in the correct position, we go backwards along arr to ensure stability
    for i in range(len(arr)-1, -1, -1):
        d = arr[i] // 10**(digit-1) % 10
        count[d] -= 1
        ind = count[d]
        sorted[ind] = arr[i]
    return sorted


print("----Count Sort Digits----")
a = [52, 21, 11, 323, 0, 46, 432, 215, 751]
print(a)
print(count_sort_digits(a, 1))


a = [231, 445, 232, 235, 123, 654, 2341, 35, 2, 34, 3, 53, 525, 353]
print(radix_sort(a))