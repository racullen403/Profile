"""
Heap Sort:

    Heap sort is a very efficient and popular sorting method, taking advantage of indexing in an array and our
    knowledge of complete binary trees.

        - Given some object at index i, we know in a complete binary tree, its left and right children would be given
        by the

            left = (2*i) + 1
            right = (2*i) + 2

        - Also given i, we know the parent can be found using

            parent = (i - 1) // 2

        - If there are n nodes in the array, then the last non-leaf node is given by the above:

            last non-leaf = (n - 1) // 2


    Using this, we can convert an array into a heap (priority queue) using the heap sort algorithm.


    Min-Heap:
        - Complete Binary Tree
        - All nodes are smaller than their children nodes.

    Heapify:
        - Starting from the last non-leaf node, find the smallest value between, i, and its left and right children, if i
        was not the smallest, we swap the smallest with i, and apply heapify again on the child node position that was
        swapped.
        - In this way, we place the smallest value at the "root" position i, and "sink" the original value at i, down
        the tree as far as it will go until it obeys the min-heap property.
        - Finally, repeat this process going backwards along the indexes until we have done index 0.

Note: This concept of "sinking" the node down to its correct position only works if the nodes below it are already
obeying the heap property. This is ensured by starting at the last non-leaf node and working backwards towards the top.

In essence, Heap Sort is just an application of the Heapify algorithm, which "sinks" a node into its correct position
in a heap.


Time Complexity:
    - O(nlogn), height of the tree is logn,in the worst case we would make logn swaps for the n/2 non-leaf nodes.

Space Complexity:
    - O(1) since all is done in place.

"""


def heap_sort(arr):

    def heapify(i):
        smallest = i
        left = (2 * i) + 1
        right = (2 * i) + 2
        if left < len(arr) and arr[left] < arr[smallest]:
            smallest = left
        if right < len(arr) and arr[right] < arr[smallest]:
            smallest = right
        if i != smallest:
            arr[i], arr[smallest] = arr[smallest], arr[i]
            heapify(smallest)

    start = (len(arr) // 2) - 1
    for j in range(start, -1, -1):
        heapify(j)


def show_heap(heap):
    """
    Left Child, Right Sib Representation
    """
    level = 0
    for i in range(len(heap)):
        if i == (2**level) - 1:
            print("\nLevel:", level, end="    ")
            level += 1
        print(heap[i], end=" ")


def example1():
    a = [5, 3, 2, 4, 6, 1, 8, 7, 9, 0]
    heap_sort(a)
    show_heap(a)


example1()

