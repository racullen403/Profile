"""
Quick Sort:

    This is another sorting algorithm based on Divide and Conquer:

        - We select an object to be the pivot, usually the right most, and sort every object up to it such that those
        less than or equal will be place on its left and those greater than will be place on its right, once the
        pivot is in place, we consider it sorted and apply the same again to the left and right sub-arrays at either
        side of the pivot.

        - This continues until sub arrays are of length one, at which point the array is sorted, and we can return
        up the "tree", combining the sorted arrays.


        E.G     Consider [4, 3, 5, 1, 2], pivot=2, swap=4

                    4 > 2 do nothing
                    3 > 2 do nothing
                    5 > 2 do nothing
                    1 < 2 so swap 1 with 4  [1, 3, 5, 4, 2], and move swap up a position, swap=3

                    Finally, we swap the pivot into its correct position [1, 2, 5, 4, 3]

                    Now we apply again to the left array [1] and right array [5, 4, 3]:


                Left array [1] is length 1 so, we know it is in position.


                Right array [5, 4, 3], pivot=3, swap=5

                    5 > 3 do nothing
                    4 > 3 do nothing
                    swap 3 into its position, [3, 4, 5]

                    apply again to left=[] and right=[4, 5]


                left=[] is done

                right=[4, 5], pivot=5, swap=4

                    4 < 5 so keep as is and increase swap position, swap=5

                    swap 5 into correct position, [4, 5]

                    apply again to left=[4] and right=[]

                left=[4] and right=[] are already sorted (length <= 1) and so we are done.


            NOTE: we can simply pass down the index of the left and right positions that define the arrays we want
            to consider, this means we can do all the swaps in-place in the original array and apply again to the
            left and right sub-arrays at either side of the pivot, when we hit l == r, we know the sub array is of
            length one and so the sub array will be sorted.

    The easiest way to understand quick sort is that we are simply choosing one object (the rightmost) and placing it
    into its correct position in the array, this is done by moving any object smaller, to its left, and any object
    larger, to its right, hence the pivot is in its final correct position. We then simply apply this again to the
    left and right sub-arrays that run from l -> pivot-1 and pivot+1 -> r.


    Space complexity is O(1) because we can you it all in place

    Time Complexity is O(nlogn), we break the array down into halves at each stage, so logn levels. And at each level
    there are n elements to look through and sort (actually less than n since the previous pivot is not included
    in the next level). 


One of the downsides to this method is that it does not retain Stability, ie the ordering or objects with the same
values may change

Another downside is that the worst case scenario is O(n^2), this happens when the pivot at every level is the largest
or smallest object, as a result, one of the sub arrays will always have 0 elements and the other n-1. However, in the
average case it is O(nlogn)

"""


def quick_sort(arr):

    def sort_about_pivot(l, r):
        pivot = r
        swap = l
        while l < r:
            if arr[l] <= arr[pivot]:
                if swap != l:
                    arr[l], arr[swap] = arr[swap], arr[l]
                swap += 1
            l += 1
        arr[swap], arr[pivot] = arr[pivot], arr[swap]
        return swap

    def sort(l, r):
        if l < r:
            pivot = sort_about_pivot(l, r)
            sort(l, pivot - 1)
            sort(pivot + 1, r)

    sort(0, len(arr) - 1)


def quick_sort_show(arr):
    print("\nOriginal Array:", arr, "\n")

    def sort_about_pivot(l, r):
        print("\nCurrent Array:", arr)
        print("\n  Pivoting", arr[l:r + 1], "about", arr[r], "\n")
        start = l
        pivot = r
        swap = l
        while l < r:
            if arr[l] <= arr[pivot]:
                if swap != l:
                    arr[l], arr[swap] = arr[swap], arr[l]
                    print("    {} <= {}, Swapping {} and {}:".format(arr[swap], arr[l], arr[swap], arr[l]), arr[start:r + 1])
                else:
                    print("    {} <= {}, already in place, increase swap position:".format(arr[l], arr[pivot]))
                swap += 1
            else:
                print("    {} > {}, go next!".format(arr[l], arr[pivot]))
            l += 1
        arr[swap], arr[pivot] = arr[pivot], arr[swap]
        print("\n  Insert Pivot, swap {} and {}:".format(arr[swap], arr[pivot]), arr[start: r + 1])
        return swap

    def sort(l, r):
        if l < r:
            pivot = sort_about_pivot(l, r)
            sort(l, pivot - 1)
            sort(pivot + 1, r)

    sort(0, len(arr) - 1)

    print("\nSorted Array:", arr)


def example():
    from random import shuffle
    a = [i for i in range(6)]
    shuffle(a)
    quick_sort_show(a)

