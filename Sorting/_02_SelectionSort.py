"""
Selection Sort:

    We iterate through the list to find the minimum object, once we reach the end, we swap the minimum with the object
    at the front, then move the front pointer forward one position, and repeat. This is very similar to bubble sort,
    except, we are only performing 1 swap on each iteration, and we are swapping to the front of the list instead
    of end.

    E.G.

        First iteration:

            Front: 5

            [5, 3, 4, 1, 2] object=5, min=5

            [5, 3, 4, 1, 2] object=3, min=3

            [5, 3, 4, 1, 2] object=4, min=3

            [5, 3, 4, 1, 2] object=1, min=1

            [5, 3, 4, 1, 2] object=2, min=1

            swap min and front [1, 3, 4, 5, 2] move front, front += 1


        Second Iteration:

            Front: 3

            [1, 3, 4, 5, 2] object=3, min=3

            [1, 3, 4, 5, 2] object=4, min=3

            [1, 3, 4, 5, 2] object=5, min=3

            [1, 3, 4, 5, 2] object=2, min=2

            swap min and front [1, 2, 4, 5, 3], move front, front += 1


        Third Iteration:

            Front: 4

            [1, 2, 4, 5, 3] object=4, min=4

            [1, 2, 4, 5, 3] object=5, min=4

            [1, 2, 4, 5, 3] object=3, min=3

            swap min and front [1, 2, 3, 5, 4], move front, front += 1


        Fourth Iteration:

        Front: 5

            [1, 2, 3, 5, 4] object=5, min=5

            [1, 2, 3, 5, 4] object=4, min=4

            swap min and front [1, 2, 3, 4, 5], move front, front += 1

        Front == end of array so DONE!


Selection sort reduces the number of swaps that occur, this means writing to memory is only O(n) whereas in bubble sort
it was O(n^2), however, we cannot stop early if the array is already sorted, we must go through each iteration in
order to ensure the minimum is at the correct position each time. This means if checking all objects is compulsory,
selection sort may be better than bubble_sort.


Space complexity O(1)

Time complexity O(n^2)

"""


def selection_sort(arr):
    front = 0
    while front != len(arr) - 1:
        minimum = front
        for i in range(front+1, len(arr)):
            if arr[i] < arr[minimum]:
                minimum = i
        arr[front], arr[minimum] = arr[minimum], arr[front]
        front += 1


def selection_sort_show(arr):
    front = 0
    while front != len(arr) - 1:
        print("\nIteration {}:".format(front + 1), "\n\n  Front:", arr[front])
        minimum = front
        for i in range(front+1, len(arr)):
            if arr[i] < arr[minimum]:
                minimum = i
            print(" ", arr, "object={}, min={}".format(arr[i], arr[minimum]))
        arr[front], arr[minimum] = arr[minimum], arr[front]
        front += 1
        print("\n  Swap {} and {}:".format(arr[minimum], arr[front-1]), arr, "\n  New Front: ", front)
    print("\nSorted Array:", arr)


# Example of the swapping process
def example1():
    a = [5, 3, 4, 1, 2]
    selection_sort_show(a)





