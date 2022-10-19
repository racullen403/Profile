"""
Binary Search:

    This is a searching algorithm that only works on an array that is already sorted. Because the objects are sorted,
    we can simply look to the middle object on each iteration, if it is smaller than what we are searching for, then
    we know we must look to the right, else the left.

    In this way we are halving the number of objects each time until we reach the last one. It will either be what we
    are looking for, or the object does not exist in the list.


    E.G         [1, 2, 3, 4, 5, 6, 7, 8, 9]  Search for 7

                - left=0, right=8, mid=(right+left)//2=4

                    at arr[4]=5 < 7 so search right side, left=mid+1

                - left=5, right=8, mid=6

                    at arr[6]=7 Done

                - We can choose the end early since we found the value


Time Complexity = O(logn)
Space Complexity = O(1)

"""


def binary_search_iterative(arr, find):
    left, right = 0, len(arr)-1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == find:
            return find
        elif arr[mid] < find:
            left = mid+1
        else:
            right = mid-1
    raise ValueError("Could not find {}".format(find))


def binary_search_recursive(arr, find):
    left, right = 0, len(arr)-1
    mid = (left + right) // 2
    if arr[mid] == find:
        return find
    elif arr[mid] < find:
        return binary_search_recursive(arr[mid+1:], find)
    else:
        return binary_search_recursive(arr[:mid], find)


def example1():
    a = [i for i in range(10)]
    print(a)
    for j in range(10):
        print(binary_search_iterative(a, j))


def example2():
    a = [i for i in range(10)]
    print(a)
    for j in range(10):
        print(binary_search_recursive(a, j))
