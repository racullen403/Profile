"""
Merge Sort:

    Sorting Algorithm based on Divide and Conquer. We divide the array into sub-arrays until a base condition is met
    (sub array of length 1), then using the sub-arrays, we sort the previous sub-array, and continue backwards until
    we sort the main one.

    E.G.   DIVIDE

                                    [5, 3, 1, 4, 2, 6]
                                  /                    \
                            [5, 3, 1]                 [4, 2, 6]
                          /           \              /         \
                    [5, 3]             [1]       [4, 2]          [6]
                   /      \                     /      \
                [5]       [3]                 [4]      [2]


            - We recursively break the array down into sub-arrays as seen above, left and right.
            - Once we reach the base condition, sub-array of length 1, we return up to the previous array
            - Now, using the two left and right sub-arrays, we sort the current array. In this way, we know the
            left and right sub-arrays will always be sorted in the recursive process, and once the current array
            is sorted, we pass it back up the "tree" as either the left or right sub-array of the previous array.
            This process will chain the whole way back to the initial array, with sorted left and right sub-arrays,
            which we can then use to sort the final array.


            CONQUER

                arr=[5, 3],    left=[5], right=[3]

                    because left is length=1, we would return to arr and then go down the right path, also length=1,
                    returning to arr=[5, 3], finally we sort arr using left=[5] and right=[3].

                        arr=[3, 5] which returns to previous array [5, 3, 1] as left=[3, 5].


                arr=[5, 3, 1],    left=[3, 5] (now sorted), right=[1]

                    we would go down the right path now, as length=1 we return and sort using left and right.

                        arr=[1, 3, 5] and return to previous array [5, 3, 1, 4, 2, 6] as left=[1, 3, 5]


                arr=[5, 3, 1, 4, 2, 6], left=[1, 3, 5] (now sorted), right= ...

                - We see how the left side was sorted, this same process would then continue down the right path
                and return right=[2, 4, 6]

                Finally arr=[1, 2, 3, 4, 5, 6]


    Space Complexity:

        At first glance you would think the space required to store all the sub-arrays would be O(nlogn), ie at every
        level of the tree we need to store all n values. However, we execute this method sequentially, not in parallel.

            Take n=16 "nodes" in the array, we will draw a tree of the number of "nodes" to store all the values
            required in our recursion calls, the worst case scenario:

                        16
                      /    \
                     8      8
                           /  \
                         4     4
                              /  \
                             2    2
                                 /  \
                                1    1


            This can be generalised to:

                Sn = n + n + n/2 + n/4 + n/8 + ... and so we know our Space Complexity < Sn

                Sn = n(1 + (1 + 1/2 + 1/4 + 1/8 + ...))


                Now consider a Taylor's Series Expansion:

                    - For some real function f(x) that is infinitely differentiable at the real number a, we can
                    express it as the following power series

                        f(x) = SUM( fn(a)/n! * (x-a)^n ) for n=0,1,2,3,... to inf, where fn(x) is the nth derivative
                        of f(x)

                    - Power Series:

                        Suppose f(x) = SUM(an * (x-a)^n) for n=0,1,2,3,...

                        f(x) = a0 + a1(x-a) + a2(x-a)^2 + a3(x-a)^3 + a4(x-a)^4 + ...
                        f(a) = a0

                        f'(x) = a1 + 2*a2*(x-a) + 3*a3(x-a)^2 + ...
                        f'(a) = a1

                        f''(x) = 2*a2 + 3*2*a3(x-a) + ...
                        f''(a) = 2*a2

                        in this way, we can sub these values and get the Taylor's Series

                        f(x) = f(a) + f'(a)*(x-a) + f''(a) / 2 * (x-a)^2 + ...


                    - Note: it is a bit more complicated, there are certain conditions for when a function can be
                    written as a power series. This just shows how we get the coefficients of a power series using
                    the Taylor's Series


            Now, Sn = n(1 + (1 + 1/2 + 1/4 + 1/8 + ...)),

                Note 1 + 1/2 + 1/4 + 1/8 + ... can be written as a power series

                Consider 1/(1-x) = 1 + x + x^2 + x^3 + ... and let x=1/2 (using Taylor's Series)

                2 = 1 + 1/2 + 1/4 + 1/8 + ...

                Hence, Sn = 3n and we know our space complexity has to be less than this,

                    Space Complexity < Sn = 3n therefore O(n) and not O(nlogn)



    Time Complexity:

        This is a little easier to understand. We know there is roof(logn) levels and at every level there will be
        the same n objects that need to be sorted. Hence, O(nlogn) time complexity



"""


def merge_sort(arr):
    if len(arr) > 1:
        mid = (len(arr) - 1) // 2
        left = arr[:mid + 1]
        right = arr[mid + 1:]
        merge_sort(left)
        merge_sort(right)
        i, i1, i2 = 0, 0, 0
        while i1 < len(left) and i2 < len(right):
            if left[i1] <= right[i2]:
                arr[i] = left[i1]
                i1 += 1
            else:
                arr[i] = right[i2]
                i2 += 1
            i += 1
        while i1 < len(left):
            arr[i] = left[i1]
            i1 += 1
            i += 1
        while i2 < len(right):
            arr[i] = right[i2]
            i2 += 1
            i += 1


def merge_sort_show(arr, step=0, side="ROOT"):
    if len(arr) > 1:
        mid = (len(arr) - 1) // 2
        left = arr[:mid + 1]
        right = arr[mid + 1:]

        print("|   " * (step + 1))
        print("|   " * step + "|---" + "STEP {}:{}".format(side, step))
        print("|   " * (step + 1) + "|   ")
        print("|   " * (step + 1) + "|---" + "DIVIDE:")
        print("|   " * (step + 1) + "|---" "arr={}, left={}, right={}".format(arr, left, right))

        merge_sort_show(left, step + 1, "LEFT")
        merge_sort_show(right, step + 1, "RIGHT")
        i, i1, i2 = 0, 0, 0
        while i1 < len(left) and i2 < len(right):
            if left[i1] <= right[i2]:
                arr[i] = left[i1]
                i1 += 1
            else:
                arr[i] = right[i2]
                i2 += 1
            i += 1
        while i1 < len(left):
            arr[i] = left[i1]
            i1 += 1
            i += 1
        while i2 < len(right):
            arr[i] = right[i2]
            i2 += 1
            i += 1

        print("|   " * (step + 2))
        print("|   " * (step + 1) + "|---" + "SOLVE {}:{}".format(side, step))
        print("|   " * (step + 1) + "|---" + "{}={}".format(side, arr))


def example():
    a = [5, 3, 2, 1, 4, 6, 9, 8, 7]
    print("Original Arr:", a)
    print("\n  ----Applying merge_sort----\n")
    merge_sort_show(a)
    print("\nSorted Arr:", a)



example()



