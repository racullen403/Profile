"""
Given an array, that is circularly linked, we must find the maximum sum of the sub-arrays it can form.

    Now remember Kadane's algorithm for finding the maximum sub array sum:

        [        MAX              ][                                        ]
        [                ][          MAX         ][                         ]
        [                                              ][        MAX        ]

        It would find the maximum sum in a similar form as above.

        def kadanes(arr):
            max_sum = arr[0]
            for i in range(1, len(arr)):
                arr[i] = max(arr[i] + arr[i-1], arr[i])
                if arr[i] > max_sum:
                    max_sum = arr[i]
            return max_sum


    Now if we want to consider the circular array, we can look to Kadane's Algorithm for inspiration. Kadane's will
    find the max_sum subarray for the case of non-circular arrays, however, we should note that if we were to calculate
    the minimum instead of the maximum, then the total_sum - minimum would also give us the maximum subarray value.

    e.g.

        [        MAX              ][                    MIN                 ]
        [   MIN1         ][          MAX         ][           MIN2          ]
        [                 MIN                          ][        MAX        ]

        MAX = TOTAL - MIN

        hence in the edges case where the maximum is formed from a circular array we get this form

                [   MAX1         ][          MIN         ][           MAX2          ]

        which we can solve as Max = Total - Min

    This tells us we need to find the maximum subarray sun using kadane's, but also the minimum subarray sum, and
    finally compare maximum from the linear list case to the maximum from the circular list case, and return the
    largest.

"""


def kadane(arr):
    max_sum = arr[0]
    for i in range(1, len(arr)):
        arr[i] = max(arr[i] + arr[i - 1], arr[i])
        if arr[i] > max_sum:
            max_sum = arr[i]
    return max_sum


def circular_kadane(arr):
    max_sum = arr[0]
    min_sum = arr[0]
    curr_max = 0
    curr_min = 0
    total = 0
    for i in range(len(arr)):
        total += arr[i]
        curr_max = max(curr_max + arr[i], arr[i])
        max_sum = max(curr_max, max_sum)
        curr_min = min(curr_min + arr[i], arr[i])
        min_sum = min(curr_min, min_sum)
    if max_sum < 0:
        return max_sum
    return max(max_sum, total - min_sum)

