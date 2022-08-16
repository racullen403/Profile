"""
Merge Sort:

    - This approach uses a divide and conquer method to create sub arrays which can be used to sort the primary array
    - We continuously break the array in half into 2 sub-arrays and store them as auxiliary arrays.
    - Do this until we reach the base condition of an array of length 1, this lets us know we have reached the bottom.
    - From here we can sort the previous array using the left and right sub-arrays and build our way back.

    e.g

                            5 6 4 3 2 1 8 7
                          /                 \
                    5 6 4 3                2 1 8 7
                    /       \              /        \
                5 6         4 3         2 1         8 7
                / \         /  \        /  \        /  \
              5    6       4    3      2   1       8   7

        Once at the bottom we can use the left and right sub arrays to sort the previous array.

        So our base cases would sort as follows

             5 6, 3 4        1 2, 7 8

        And then we would use these left-right sub-array pairs to sort the array "above"

            3 4 5 6,    1 2 7 8

        Finally we are left with the last left-right pair which will sort our final solution

            1 2 3 4 5 6 7 8
"""
import random


def merge_sort(a):
    if len(a) > 1:
        mid = len(a)//2
        left = a[:mid]
        right = a[mid:]
        merge_sort(left)
        merge_sort(right)
        i_l = i_r = i = 0
        while i_l < len(left) and i_r < len(right):
            if left[i_l] <= right[i_r]:
                a[i] = left[i_l]
                i_l += 1
            else:
                a[i] = right[i_r]
                i_r += 1
            i += 1
        while i_l < len(left):
            a[i] = left[i_l]
            i += 1
            i_l += 1
        while i_r < len(right):
            a[i] = right[i_r]
            i += 1
            i_r += 1


def example_merge_sort():
    mylist = list(range(10))
    random.shuffle(mylist)
    print("Initial List: ", mylist)
    merge_sort(mylist)
    print("Sorted List: ", mylist)


# example_merge_sort()


def test_merge_sort(n=1000):
    sol = list(range(-100, 100))
    for test in range(1000):
        test_list = list(range(-100, 100))
        random.shuffle(test_list)
        merge_sort(test_list)
        if test_list != sol:
            return False
    return True


# print(test_merge_sort())