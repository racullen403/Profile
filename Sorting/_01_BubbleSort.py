"""
Bubble Sort:

    This is the most basic form of sorting, we use a pointer for the current object (starting at 0) and a pointer for
    the last position of the array.

        - Simply swap current object with the next object if it is larger, then move pointer to next position.
        - Continue like this until our pointer is at the final position pointer.
        - Repeat but move final position pointer back one space and object pointer to the start.
        - Repeat until final pointer is at index 0.

    We are essentially swapping adjacent objects until the largest one "bubbles" through to its
    final position, then reducing the final position by 1, and repeating.

        E.G.

            first iteration:

                [4, 3, 5, 2, 1] object=0, end=4

                [3, 4, 5, 2, 1] object=1, end=4

                [3, 4, 5, 2, 1] object=2, end=4

                [3, 4, 2, 5, 1] object=3, end=4

                [3, 4, 2, 1, 5] object=4, end=4

                object == end so end -= 1


            second iteration:

                [3, 4, 2, 1, 5] object=0, end=3

                [3, 4, 2, 1, 5] object=1, end=3

                [3, 2, 4, 1, 5] object=2, end=3

                [3, 2, 1, 4, 5] object=3, end=3

                object == end so end -= 1


            third iteration:

                [3, 2, 1, 4, 5] object=0, end=2

                [2, 3, 1, 4, 5] object=1, end=2

                [2, 1, 3, 4, 5] object=2, end=2

                object == end so end -= 1


            fourth iteration:

                [2, 1, 3, 4, 5] object=0, end=1

                [1, 2, 3, 4, 5] object=1, end=1

                object == end so end -= 1


            fifth iteration:

                [1, 2, 3, 4, 5] object=0, end=0

                DONE!


Space complexity is O(1) since this happens in place.

Time complexity is O(n^2):

    Take n objects, each loop does 1 less comparison so the total comparisons will be

        Sn = (n-1) + (n-2) + (n-3) + ... + 2 + 1

    Now consider the following general partial series:

        Sn = n + (n-1) + (n-2) + ... + 2 + 1

        2Sn = n + (n-1) + (n-2) + ... +   2   +   1

                    1   +   2   +     + (n-2) + (n-1) + n

        2Sn = 2n + (n-1)n

        2Sn = n(n+1)

        Sn = n(n+1)/2

    So in our case we use (n-1) instead of n and find Sn = n(n-1)/2 ~ O(n^2)


    Note: This can be generalised further (arithmetic progression)

        Sn = a1 + a2 + a3 + ... + an-1 + an  Where an = an-1 + d, d is the constant difference between terms

            Sn = a1 + (a1 + d) + (a1 + 2d) + ... + (a1 + n-2*d) + (a1 + (n-1)*d)

            Or

            Sn = an + (an - d) + (an - 2d) + ... + (an - (n-2)*d) + (an - (n-1)*d)

        So

        2Sn = a1 + (a1 + d) + (a1 + 2d) + ... + (a1 + n-2*d) + (a1 + (n-1)*d)
             +an + (an - d) + (an - 2d) + ... + (an - (n-2)*d) + (an - (n-1)*d)

        2Sn = (a1 + an) + (a1 + an) + ... + (a1 + an) + (a1 + an)

        2Sn = n*(a1 + an)

        Sn = n*(a1 + an)/2


Further Optimisation:

    Regardless of whether the array is sorted or not, this will do all the comparisons. We can
    change this by introducing a flag, swap=False. We change this to True if a swap occurs, if no
    swap occurs it remains False, and we know the array is sorted

"""


def bubble_sort(array):
    end = len(array) - 1
    swap = True
    while end != 0 and swap:
        swap = False
        for i in range(0, end):
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swap = True
        end -= 1


def bubble_sort_show(array):
    print("Original:", array)
    end = len(array) - 1
    swap = True
    while end != 0 and swap:
        print("\nIteration {}:".format(len(array) - end))
        swap = False
        for i in range(0, end):
            print("  ", array, "object={}, end={}".format(i, end))
            if array[i] > array[i + 1]:
                array[i], array[i + 1] = array[i + 1], array[i]
                swap = True
        print("  ", array, "object={}, end={}".format(end, end))
        end -= 1
    print("\nDONE:", array)


# Example of sort
def example1():
    b = [4, 3, 5, 2, 1]
    bubble_sort_show(b)


# Example of swap flag
def example2():
    a = [1, 2, 3, 5, 4]
    bubble_sort_show(a)


