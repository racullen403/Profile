"""
The alternative to a linked list is the heap data structure, this uses a tree structure to organise the data. We
can use either a Min-Heap or a Max-Heap, note that the tree structure can arise from either the indexes of an
array, or the pointers of Nodes in a complete binary tree.

    - A Min-Heap has the property that for any given Node, it's child Nodes will be larger, this
    property cascades down the tree, excluding the leaf nodes. ANd the root node is always the smallest.

    - Max-Heap is the same but child Nodes are smaller than parent and root is largest.

    E.G.    Min-Heap

                                    [ (1)A ]
                                     /    \
                             [ (1)B ]       [ (2)C ]
                          /        \        /        \
                   [ (2)D ]    [ (2)E ]  [ (2)F ]    [ 2(G) ]

            This is the general structure of a binary Min-Heap, in Node form (it can also be represented by a list
            and indexes used to find children, since the heap is a complete tree).

    - The heap is a complete binary tree, meaning all levels of the tree are completely filled, except possibly the
    leaf nodes, which will always fill from the left (a left sibling at the end may not have a right sibling, it does
    not have to be a full binary tree).


Using Indexes:

    - Given an array and an object at index i, we know where its left and right children should be

            left child -> 2i + 1
            right child -> 2i + 2

    - If we know there are n objects in the array, then the first non-leaf node is given by

            first non-leaf -> n//2 - 1

    - With this information we can convert a regular list of unstructured objects and their priorities, into a heap.

    - Starting from the first non-leaf node, we heapify each node from index (n-1)//2 back to 0.

    - Heapify:

        Starting from the first non-leaf node, we structure it into a heap, ie swap nodes so that root > or < both
        children.

        If a swap takes place, we have to then look at the node that got moved down the tree, as this may break
        the heap structure of the lower node-children pairs. We continuously do this for each node until we reach
        the bottom of the tree, then move onto the next non-leaf node and repeat

        (note that in worst case it can be shown the time complexity  Sn <= O(nlogn)).

            let h = floor(logn) be the height of tree
            let d = floor(log(i+1)) be the depth of node

            then Sn = Sum(h-d) for i = 0 to i = n//2 - 1

            We get Sn = (n//2 - 1)h - Sum(d) for i = 0 to i = n//2 - 1

            So Sn <= (n//2 - 1)h < n*floor(logn) < nlogn

    - Enqueue:

        We simply need to add the object to the end of the heap, and then "swim" it as high as it can go.

        We could also heapify the whole structure, however, this would take nlogn time, whereas to swim the new node
        up at worst will take logn.

        Note that this "swim" method, is only viable on an already structured heap

    - Dequeue:

        To get the next object out of the queue, we swap the head object with the very last object in the heap, and
        then pop it out.

        Now we have to deal with this swapped term, we can simply apply our heapify method at the root, this will run
        in O(logn) here since there are a maximum of h swaps from the root node to a leaf position.

        The main issue with this is that we lose the order that the objects come in by doing the swap with the last
        term. One way to fix this would be to use time of insertion as a 2nd priority for 2 objects with the same
        initial priority.

    - Removal:

        In order to remove a node, we would need to traverse the tree until we find the node, then swap it with the
        last object and pop it, then we would need to heapify the structure again.

        This potentially would take O(n) time. An alternative would be to create an auxiliary array that contains
        objects to be removed, if an object is dequeued and found in this array, we ignore it.

        This solution cuts down the removal to O(1), however, we need extra space to hold the removal objects and the
        heap itself will have the extra useless information.

        Note that instead of heapify the whole structure after the swap, since the structure is already in a heap
        form, we simply have to look at the position of the swap, and decide if this new node needs to "swim" up
        the heap, or "sink" down it (sinking is just the normal heapify method).
"""


class MinHeapArray:

    def __init__(self, list_to_heapify=None):
        """
        list_to_heapify: a list of tuples, tuple (priority, object), where priority is an integer, and object is
        what is being queued
        """
        if list_to_heapify:
            self.heap = list_to_heapify
            for i in range((len(self.heap) // 2) - 1, -1, -1):
                self.heapify(i)
        else:
            self.heap = []

    def is_empty(self):
        return self.heap == []

    def heapify(self, index):
        if (2 * index) + 1 > len(self.heap):  # Node is a leaf or non-existent, we can't heapify
            return
        else:
            left = (2 * index) + 1
            right = (2 * index) + 2
            min_prio = index
            if self.heap[left][0] < self.heap[min_prio][0]:
                min_prio = left
            if right < len(self.heap) and self.heap[right][0] < self.heap[min_prio][0]:  # We check right exists first
                min_prio = right
            if min_prio == index:  # If already a heap, we are done as we know lower levels are already a heap
                return
            else:
                self.heap[index], self.heap[min_prio] = self.heap[min_prio], self.heap[index]  # Swap to ensure heap
                self.heapify(min_prio)  # Heapify swapped term

    def enqueue(self, priority, val):
        self.heap.append((priority, val))
        self.swim(len(self.heap)-1)

    def swim(self, index):
        if index == 0:
            return
        else:
            parent = (index - 1) // 2
            if self.heap[parent][0] > self.heap[index][0]:
                self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
                self.swim(parent)
            else:
                return

    def dequeue(self):
        if self.is_empty():
            raise ValueError("Queue is empty!")
        else:
            self.heap[0], self.heap[len(self.heap)-1] = self.heap[len(self.heap)-1], self.heap[0]
            temp = self.heap.pop()
            self.heapify(0)
            return temp

    def remove(self, val):
        if self.is_empty():
            raise ValueError("Queue is empty")
        i = 0
        while i < len(self.heap) and self.heap[i][1] != val:
            i += 1
        if i == len(self.heap):
            raise ValueError("Could not find object")
        else:
            self.heap[i], self.heap[len(self.heap)-1] = self.heap[len(self.heap)-1], self.heap[i]
            self.heap.pop()
            parent = (i - 1) // 2
            if self.heap[i] < self.heap[parent]:
                self.swim(i)
            else:
                self.heapify(i)

    def show(self):
        n = len(self.heap)
        h = 0
        while n != 1:
            n = n//2
            h += 1
        print("\nMin-Heap, height", h)
        for layer in range(h+1):
            print("  Layer:", layer, end="    ")
            print("    [", end=" ")
            for i in range((2**layer)-1, (2**(layer+1)-1)):
                if i < len(self.heap):
                    print("({}){}".format(self.heap[i][0], self.heap[i][1]), end=" ")
            print("]")


def example1():
    # Using the heapify method
    objects = [(1, "A"), (1, "B"), (1, "C"), (2, "D"), (3, "E"), (1, "F"), (0, "G")]
    mh = MinHeapArray(objects)
    mh.show()


def example2():
    # Using the swim method
    objects = [(1, "A"), (1, "B"), (1, "C"), (2, "D"), (3, "E"), (1, "F"), (0, "G")]
    mh = MinHeapArray()
    for obj in objects:
        mh.enqueue(obj[0], obj[1])
    mh.show()


def example3():
    # Dequeue from heap, you can see how (1, "C") skips queue
    objects = [(1, "A"), (1, "B"), (1, "C"), (2, "D"), (3, "E"), (1, "F"), (0, "G")]
    mh = MinHeapArray(objects)
    mh.show()
    print("\nDequeue:", mh.dequeue())
    mh.show()


def example4():
    # Removing "E", showing the "swim" effect
    objects = [(10, "A"), (30, "B"), (20, "C"), (40, "D"), (50, "E"), (21, "F"), (25, "G")]
    mh = MinHeapArray(objects)
    mh.show()
    mh.remove("E")
    mh.show()
