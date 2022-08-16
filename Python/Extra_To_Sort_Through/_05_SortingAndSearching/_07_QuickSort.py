"""
Quick Sort:

    - This method uses a divide and conquer approach to sort the array
    - We first choose a pivot element, ie the furthest right number.
    - We then divide the array into 2 sub-arrays, the left array will have all elements smaller than (or equal to) the
    pivot, and the right array will have all elements greater than the pivot, with the pivot swapped into its correct
    position.
    - We then apply the same method onto the left and right portions of the array until we reach some base case, when
    the base case is reached, all the pivot elements will be sorted into their correct positions


    e.g

        4, 5, 2, 1, 6, 3        Pivot=3, swap_index=0,  everytime an element is <=3 we swap it with the swap position
                                                        and add 1 to this index
                                4>3 so leave
                                5>3 so leave
                                2<3 so swap and increase index , swap_index=1
        2, 5, 4, 1, 6, 3        1<3 so swap and increase index, swap index=2
        2, 1, 4, 5, 6, 3        6>3 so leave
                                We have reached the end so we swap the pivot with in the index position
        2, 1 |3| 5, 6, 4        So 3 is now sorted into its correct position, we apply this same method on the left
                                    and right sub-arrays

        |1| 2 |3| |4| 5, 6

        |1| |2| |3| |4| |5| 6

        |1| |2| |3| |4| |5| |6| DONE

"""
import random


def partition(a, l, r):
    if l < r:
        pivot = a[r]
        swap_index = l
        for i in range(l, r):
            if a[i] <= pivot:
                a[i], a[swap_index] = a[swap_index], a[i]
                swap_index += 1
        a[swap_index], a[r] = a[r], a[swap_index]
        return swap_index


def quick_sort(a, l, r):
    if l < r:
        p = partition(a, l, r)
        quick_sort(a, l, p-1)
        quick_sort(a, p+1, r)


def example_quick_sort():
    mylist = list(range(10))
    random.shuffle(mylist)
    print("My List: ", mylist)
    quick_sort(mylist, 0, len(mylist)-1)
    print("Sorted List: ", mylist)


# example_quick_sort()


def test_quick_sort(n=1000):
    sol = list(range(-100, 100))
    for test in range(1000):
        test_list = list(range(-100, 100))
        random.shuffle(test_list)
        quick_sort(test_list, 0, len(test_list)-1)
        if test_list != sol:
            return False
    return True

# print(test_quick_sort())