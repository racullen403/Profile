"""
Insertion Sort:

    This sort places objects in a suitable position on each iteration, working similar to how we would sort a hand of
    cards.

        - Assume first object is sorted
        - If next object is larger than previous, leave it in place and move onto the next.
        - If it was smaller, then save the object, start shifting each object to its left, one position right, until
        we find an object that is smaller than our saved one, this will be its correct position and insert it here.
        - Repeat this process until we reach the end of the array.

        E.G

            Consider [5, 3, 4, 1, 2], assume 5 is in correct position.

                [5, 3, 4, 1, 2] object=3

                    3 < 5, shift 5 right, [5, 5, 4, 1, 2]

                    Reached end, insert object, [3, 5, 4, 1, 2]


                [3, 5, 4, 1, 2] object=4

                    4 < 5, shift 5 right, [3, 5, 5, 1, 2]

                    4 > 3, insert object, [3, 4, 5, 1, 2]


                [3, 4, 5, 1, 2] object=1

                    1 < 5, shift 5 right, [3, 4, 5, 5, 2]

                    1 < 4, shift 4 right, [3, 4, 4, 5, 2]

                    1 < 3, shift 3 right, [3, 3, 4, 5, 2]

                    Reached end, insert object, [1, 3, 4, 5, 2]


                [1, 3, 4, 5, 2] object=2

                    2 < 5, shift 5 right, [1, 3, 4, 5, 5]

                    2 < 4, shift 4 right, [1, 3, 4, 4, 5]

                    2 < 3, shift 3 right, [1, 3, 3, 4, 5]

                    2 > 1, insert object, [1, 2, 3, 4, 5]

                DONE!


Space complexity O(1)

Time Complexity O(n^2), best case would be O(n), all objects are sorted already or close.

"""


def insertion_sort(arr):
    for i in range(1, len(arr)):
        obj = arr[i]
        while i > 0 and arr[i - 1] > obj:
            arr[i] = arr[i - 1]
            i -= 1
        arr[i] = obj


def insertion_sort_show(arr):
    print("\nOriginal Array:", arr)
    for i in range(1, len(arr)):
        obj = arr[i]
        print("\n", arr, "object={}".format(arr[i]), "\n")
        while i > 0 and arr[i - 1] > obj:
            print("    {} < {}, shift {} right,".format(arr[i], arr[i - 1], arr[i-1]), end=" ")
            arr[i] = arr[i - 1]
            print(arr)
            i -= 1
        arr[i] = obj
        if i == 0:
            print("    Reached end, insert object,", arr)
        else:
            print("    {} > {}, insert object,".format(arr[i], arr[i - 1]), arr)
    print("\nSorted Array:", arr)


def example1():
    a = [5, 3, 4, 1, 2]
    insertion_sort_show(a)

