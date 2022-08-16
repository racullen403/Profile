"""
Shell sort improves on insertion sort by breaking the list into smaller sub-lists which are then sorted using the
insertion sort. We use an increment, i, called a "gap", to create the sub-lists that are the items separated by the gap.

    E.g

        We have a list of length 9 a=[9, 8, 7, 6, 5, 4, 3, 2, 1], we choose i=3 which would create sub-lists separated
        by length 3 and then apply insertion sort.

        [{9}, 8, 7, {6}, 5, 4, {3}, 2, 1]

        sub-list 1 -> 9,6,3 after insertion sort on this sublist we get

        [3, 8, 7, 6, 5, 4, 9, 2, 1]

        We then apply again, 1 position to the right, [3, {8}, 7, 6, {5}, 4, 9, {2}, 1]

        [3, 2, 7, 6, 5, 4, 9, 8, 1]

        And one final time for the last sublist, [3, 2, {7}, 6, 5, {4}, 9, 8, {1}]

        [3, 2, 1, 6, 5, 4, 9, 8, 7]

        We see that although the list is not completely sorted, the items are now very close to where they belong.
        We now do a final insertion sort of increment 1 so finish the sort.

"""

def insertion_sort(a):
