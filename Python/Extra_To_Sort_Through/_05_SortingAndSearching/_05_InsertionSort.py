"""
Insertion Sort:

    - For this method we assume the first item to already be sorted.
    - We then look at the next item and store it, if the item to the left is larger than it, then we move that item
    right, and look at the next item to the left, repeating until we find an item that is <= to our stored item, this
    indicates we have found the stored items position.
    - Continue in this way until we have sorted the array

    e.g

        5, 3, 2, 6, 4       Assume 5 to be sorted, store=3, 3<5 so move 5 right
        5, 5, 2, 6, 4       There is no item left of 5 so we have found the final position, place 3 here
        3, 5, 2, 6, 4       Store=2, 2<5 so move 5 right
        3, 5, 5, 6, 4       2<3 so move 3 right
        3, 3, 5, 6, 4       At final position so place 2 here
        2, 3, 5, 6, 4       Store=6, 6>5 so in correct position
        2, 3, 5, 6, 4       Store=4, 4<6 so move 6 right
        2, 3, 5, 6, 6       4<5 so move 5 right
        2, 3, 5, 5, 6       4>3 so we found its position
        2, 3, 4, 5, 6       Done
"""
import random


def insertion_sort(a):
    for i in range(len(a)):
        store = a[i]
        j = i-1
        while j >= 0 and a[j] > store:
            a[j+1] = a[j]
            j -= 1
        a[j+1] = store


def example_insertion_sort():
    a = list(range(10))
    random.shuffle(a)
    print("\nInitial random list: ", a, end="\n\n")
    for i in range(len(a)):
        store = a[i]
        print("\nCurrent iteration:", a, "Store={}".format(store), "Index={}".format(i))
        j = i-1
        while j >= 0 and a[j] > store:
            print("   {} > {}, Shift Right: ".format(a[j], store), end=" ")
            a[j+1] = a[j]
            j -= 1
            print(a)
        a[j+1] = store
        print("   Final Position:", j+1, a)


# example_insertion_sort()


def test_insertion_sort(n=1000):
    for test in range(n):
        sol = list(range(-100, 100))
        test_list = list(range(-100, 100))
        random.shuffle(test_list)
        insertion_sort(test_list)
        if test_list != sol:
            return False
    return True

print(test_insertion_sort())