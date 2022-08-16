"""
Searching is the process of trying to find a particular item in a collection of items, it will
usually return either True or False.

The most common search is the "in" operator in python. It is easy to use, but we are interested
in the underlying processes for actually finding the item.


Sequential Search:

    When data is stored in a collection like a list, we say it is linear/sequential, each item has 
    a position relative to others given by the index. These index values are ordered, allowing us 
    to sequentially go through each item 1 by 1.
    
    This method iterates through the entire unordered collection and so has run time O(n) worst case,
    if the collection was to be ordered, it would increase the efficiency of a False result as we
    can determine earlier if the item is not in the list, however, the initial sorting of the
    list would increase complexity.


Binary Search:

    Consider now for an ordered list, we start by checking the middle item, if it is larger than the
    item we are searching for then we only have to look at the terms left of the middle one, if it is
    smaller then we look to the right. We then repeat this process until we find our item or  are
    left with one item, if it is not the one we are looking for then return False.
    
    Binary search only works for a sorted list. It is much more efficient as we are essentially 
    halving the items each time until be find the result. This makes this searching process run 
    in logarithmic time O(logn), going from 10 to 100 items would only double the time, similarly 
    100 to 1000 would only double the time (instead of 10x time for a linear process).

    In the recursive case below we used index slicing for the list reduction, this process takes
    O(k) each recursive call. We can fix this by simply passing the front and back index into
    the recursive call, this way we aren't changing the list at all, instead we are simply changing
    the pointers for the front and back index until either the middle points to the item we are
    looking for or the front and back are the same index and said item is not what we are looking for.
"""


def sequential_search_unordered(item, collection):
    index = 0
    while index < len(collection):
        if collection[index] == item:
            return True 
        index += 1
    return False

# print(sequential_search_unordered(12, [4, 4, 2, 56, 23, 12, 3]))
# print(sequential_search_unordered(13, [4, 4, 2, 56, 23, 12, 3]))


def sequential_search(item, collection):
    index = 0
    sorted_list = sorted(collection)
    while index < len(collection) and sorted_list[index] <= item:
        if sorted_list[index] == item:
            return True
        index += 1
    return False

# print(sequential_search(12, [1, 4, 5, 2, 3, 56, 43, 12, 23]))


def binary_search(item, collection):
    found = False
    i = 0
    j = len(collection) - 1
    while i <= j and not found:
        middle = (i+j)//2
        if collection[middle] == item:
            found = True
        if collection[middle] < item:
            i = middle + 1
        else:
            j = middle - 1
    return found

# print(binary_search(9, [1, 2, 3, 4, 5, 6, 7, 8, 9]))


# recursive binary search
# Base case is when we either find the item or the list is reduced to 0 size
# On each recursive call we are reducing the list to the left or right of the middle item
def binary_search_recursive(item, collection):
    if len(collection) == 0:
        return False
    else:
        middle = len(collection) // 2
        if collection[middle] == item:
            return True
        else:
            if collection[middle] < item:
                return binary_search_recursive(item, collection[middle+1:])
            else:
                return binary_search_recursive(item, collection[:middle])

        
# print(binary_search_recursive(11, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
# print(binary_search_recursive(1, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
# print(binary_search_recursive(9, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
# print(binary_search_recursive(7, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
# print(binary_search_recursive(2, [1, 2, 3, 4, 5, 6, 7, 8, 9]))

def binary_search_recursive_efficient(item, collection, front=None, back=None):
    # Setup
    i = front
    if front is None:
        i = 0
    j = back
    if back is None:
        j = len(collection) - 1
    # Execution
    if i == j and collection[i] != item:
        return False
    else:
        middle = (i+j)//2
        if collection[middle] == item:
            return True
        else:
            if collection[middle] < item:
                return binary_search_recursive_efficient(item, collection, front=middle+1, back=j)
            else:
                return binary_search_recursive_efficient(item, collection, front=i, back=middle-1)


print(binary_search_recursive_efficient(11, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(binary_search_recursive_efficient(1, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(binary_search_recursive_efficient(9, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(binary_search_recursive_efficient(7, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
print(binary_search_recursive_efficient(2, [1, 2, 3, 4, 5, 6, 7, 8, 9]))