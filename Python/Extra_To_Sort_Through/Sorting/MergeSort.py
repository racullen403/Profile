"""
Merge Sort:
    - Divide and Conquer, split problem into sub-problems, solve the sub-problems, combine
    solutions to sub-problems to get overall solution.
    - Use Divide and Conquer approach, split array in half into left and right array until
    they are of size _01_BasicPython.
    - Create 3 indexes l for left array, r for right array, main for main array.
    - Reconstruct new sorted arrays from solutions to sub-problems

    eg                      [5, 4, 3, 2, _01_BasicPython]
                            /              \
                        [5, 4]              [3, 2, _01_BasicPython]
                        /   \                /      \
                    [5]     [4]            [3]      [2, _01_BasicPython]
                     |       |              |        /  \
                    [5]     [4]            [3]      [2]  [_01_BasicPython]    <- Recurrence brings down to here
                       \   /                |        \   /
                    [4, 5]                 [3]       [_01_BasicPython, 2]     <- We then recreate sorted arrays
                        \                   \           /
                         [4, 5]              [_01_BasicPython, 2, 3]
                              \                /
                                [_01_BasicPython, 2, 3, 4, 5]


Complexity:
    - Time, O(nlogn), out performs InsertionSort for large inputs
    - Space O(n) to store the left and right sub-problems

Stable
"""


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr)//2
        left_arr = arr[:mid]
        right_arr = arr[mid:]
        merge_sort(left_arr)
        merge_sort(right_arr)

        l = r = main = 0
        while l < len(left_arr) and r < len(right_arr):
            if left_arr[l] <= right_arr[r]:
                arr[main] = left_arr[l]
                l += 1
                main += 1
            else:
                arr[main] = right_arr[r]
                r += 1
                main += 1

        while l < len(left_arr):
            arr[main] = left_arr[l]
            l += 1
            main += 1

        while r < len(right_arr):
            arr[main] = right_arr[r]
            r += 1
            main += 1
    return arr

print(merge_sort([5, 4, 3, 2, 1]))