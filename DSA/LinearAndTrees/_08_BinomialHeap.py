"""
Binomial Heap:

    This is an extension of the Binary Heap but provides faster union and merge operations, if we don't require the
    merge operations, then a normal Binary Heap is used, this is because the Union of two binary heaps runs in O(n)
    whereas in a Binomial Heap it is O(logn).

    Construction of Tree:
        - A binomial tree of order 0 is simply a single node.
        - A binomial tree of order k is made by taking two binomial tree of order k-1 and making one the
        leftmost child of the other

    Properties for tree of order k:
        - Contains 2^k nodes
        - Has k depth
        - At depth i, there are, iCk nodes, where C is the binomial coefficient (number of ways we can choose i
        elements from k, (k! / (i! * (k-i)!)))
        - The root will have order k, and from left to right, child nodes have order k-1, k-1, ..., 0


    The Binomial Heap:
        This is a set of Binomial Trees, where each tree follows the Min-Heap property and there can be at most one
        tree of any degree. We represent this in a root list, where roots are organised in a linked list of increasing
        degree.

        Binary Representation: If there are n nodes in the Binomial Heap, then we know there will be a as many
            Binomial Trees as there are bits "1" in the binary representation of n, furthermore, their corresponding
            bit position will give the order of the trees.

            E.G.
                    n = 13, binary = 1101,

                    so the corresponding Binomial Heap will have Binomial Trees of order 3, 2, and 0.


        Operations: The main operation is Union, most other operations call this to combine 2 binomial heaps.

            - Insert: This creates a new Binomial Heap with a Binomial Tree of order 0, and then calls the Union
            method on the original heap and the new one. O(logn)

            - Get Min: This requires us to traverse all the roots in the heap and return the smallest root
            node, O(logn). We can optimise this by having a pointer that keeps track of the min node making it O(1)

            - Extract Min: We call Get Min to return the smallest root node. We then remove it and add all its
            children into a new Binomial Heap, finally, call union on the new heap with the original. O(logn)

            - Delete: Traverse to find key, set is smaller than minimum, heapify and extract min. O(logn)

            - Decrease key: Traverse to key, reduce key's value, compare to parent, if parent is larger
            then swap and recur O(logn)

            - Union: First merge the two heaps into one, in non-decreasing order respective of root nodes O(logn).
            Now make sure there is only one tree of each order, to do this, keep track of prev_x, x, and next_x:

                    - Case 1: x and next_x are different order, move on.

                    - Case 2: x and next_x are the same order, where next_x and next_next_x are also the same order,
                    move on.

                    - Case 3: x and next_x are the same order, but next_next_x is different, if key of x is larger
                    than the key of next_x, make x the left child of next_x, else make next_x the left child of x.


    Tree representation:
        The best way to store this is a single node with the value of the key (priority level), and 2 pointers, one
        to the left most child and the other to the right sibling, we called this left child right sibling
        representation.

        The heap will simply be a series of these binomial trees, using the right sibling pointer to connect them.
"""


class BinomialTree:

    def __init__(self, val=0):
        self.val = val
        self.order = 0
        self.parent = None
        self.right_sib = None
        self.left_child = None


class BinomialHeap:

    def __init__(self):
        """
        Define the new Binomial Heap. O(1)
        """
        self.head = None

    def is_empty(self):
        """
        Tells us if heap is empty or not. O(1)
        """
        return self.head is None

    def find_min(self):
        """
        Returns the root node that is the minimum. O(logn)
        """
        if self.is_empty():
            raise ValueError("Heap is empty")
        else:
            temp = self.head
            minimum = self.head
            while temp:
                if temp.val < minimum.val:
                    minimum = temp
                temp = temp.right_sib
            return minimum

    def delete_key(self, key):
        """
        Traverse to node containing key, make its val smaller than the minimum, then swap values with parent nodes
        until we reach the root, finally, extract min.

        Note, decrease key works the same except we stop when the decreased val has reached its correct place.
        """
        if self.is_empty():
            raise ValueError("Heap is empty")
        to_visit = [self.head]
        node = None
        while to_visit:
            node = to_visit.pop()
            if node.val == key:
                to_visit = None
            else:
                if node.left_child:
                    to_visit.append(node.left_child)
                if node.right_sib:
                    to_visit.append(node.right_sib)
        if node.val != key:
            raise ValueError("Could not find key")
        else:
            min_val = self.find_min().val - 1
            node.val = min_val
            while node.parent and node.val < node.parent.val:
                parent = node.parent
                temp = node.val
                node.val = parent.val
                parent.val = temp
                node = node.parent
            return self.extract_min()

    def extract_min(self):
        """
        Extracts the min node from the heap and returns pointer to it
        """
        if self.is_empty():
            raise ValueError("Heap is empty")
        # Find node before the minimum node
        temp = BinomialTree(self.head.val)
        temp.right_sib = self.head
        prev_min = temp
        while temp.right_sib:
            if temp.right_sib.val < prev_min.val:
                prev_min = temp
            temp = temp.right_sib
        minimum = prev_min.right_sib
        if prev_min.right_sib == self.head:
            self.head = self.head.right_sib
        else:
            prev_min.right_sib = minimum.right_sib
        # Create new heap and add min's child if exists
        if minimum.order == 0:
            return minimum
        else:
            # Reverse children list so order is increasing
            new_heap = BinomialHeap()
            reverse = None
            heap = minimum.left_child
            while heap:
                temp = heap
                heap = heap.right_sib
                temp.right_sib = reverse
                reverse = temp
            new_heap.head = reverse
            self.head = self.union(new_heap)
            return minimum

    def insert(self, val):
        """
        Inserts val into the Binomial Heap. O(1) to create node, and O(logn) for union
        """
        if self.is_empty():
            self.head = BinomialTree(val=val)
        else:
            new_tree = BinomialTree(val)
            new_heap = BinomialHeap()
            new_heap.head = new_tree
            self.head = self.union(new_heap)

    def union(self, heap):
        """
        Combines self.head and another heap, "heap", into one binomial heap and sets self.heap equal to it. O(logn)
        """
        new_heap = BinomialHeap()
        new_heap.head = self.merge_heaps(heap)
        prev_x = None
        x = new_heap.head
        next_x = x.right_sib
        while next_x:
            if x.order != next_x.order or (next_x.right_sib and next_x.right_sib.order == x.order):
                prev_x = x
                x = next_x
            elif x.val <= next_x.val:
                x.right_sib = next_x.right_sib
                self.join_trees(x, next_x)
            else:
                x.right_sib = next_x.right_sib
                next_x.right_sib = x
                if prev_x is None:
                    new_heap.head = next_x
                else:
                    prev_x.right_sib = next_x
                self.join_trees(next_x, x)
                x = next_x
            next_x = x.right_sib
        return new_heap.head

    def merge_heaps(self, heap):
        """
        Merges current BinomialHeap, self.head, with another BinomialHeap, heap. Organises the BinomialTrees in a new
        heap by order, smallest to largest. In the case of equal orders, self.head nodes will be placed to the left of
        heap nodes. Finally, returns the head of the new formed heap. O(log m+n)
        """
        new_heap = BinomialHeap()
        new_heap.insert(0)
        temp = new_heap.head
        h1 = self.head
        h2 = heap.head
        while h1 and h2:
            h1.parent = None
            h2.parent = None
            if h1.order <= h2.order:
                temp.right_sib = h1
                h1 = h1.right_sib
            else:
                temp.right_sib = h2
                h2 = h2.right_sib
            temp = temp.right_sib
        while h1:
            temp.right_sib = h1
            h1 = h1.right_sib
            temp = temp.right_sib
        while h2:
            temp.right_sib = h2
            h2 = h2.right_sib
            temp = temp.right_sib
        return new_heap.head.right_sib

    def join_trees(self, tree1, tree2):
        """
        tree1 and tree2 are BinomialTree's, it will make tree2 the left child of tree1. O(1)
        """
        if tree1.order != tree2.order:
            raise ValueError("Both trees must have equal orders")
        else:
            tree1.right_sib = tree2.right_sib
            tree2.right_sib = tree1.left_child
            tree2.parent = tree1
            tree1.left_child = tree2
            tree1.order += 1

    def show(self):
        """
        Built using bfs at each root to show the individual trees
        """
        print("--------------")
        print("Binomial Heap:")
        print("--------------")
        temp = self.head
        roots = []
        while temp:
            roots.append(temp)
            temp = temp.right_sib

        def bfs_show(count, sep):
            space = "     "
            indent = "|     "
            if len(to_visit) > 0:
                node = to_visit.pop()
                print(node.val, end="")
                if node.left_child:
                    to_visit.append(node.left_child)
                    count += 1
                if node.right_sib:
                    to_visit.append(node.right_sib)
                    print(" --- ", end="")
                    bfs_show(count, sep)
                else:
                    print()
                    print(sep * space, end=" ")
                    print(indent * count)
                    print(sep * space, end=" ")
                    count -= 1
                    print(indent * count, end="")
                bfs_show(count, sep)

        for root in roots:
            print("\n     Tree, Order {}:".format(root.order))
            print("\n          ", root.val)
            print("           |")
            print("           ", end="")
            if root.left_child:
                to_visit = [root.left_child]
                bfs_show(0, 2)


# Show Insertion
def example():
    bh = BinomialHeap()
    a = [i for i in range(16)]
    for i in a:
        bh.insert(i)
        print("\n\nInsert {}:".format(i))
        bh.show()


# Show Extract Min
def example2():
    import random
    bh = BinomialHeap()
    a = [random.randrange(0, 16) for i in range(16)]
    for i in a:
        bh.insert(i)
    bh.show()
    while bh.head:
        m = bh.extract_min()
        print("\n\nExtract Min:", m.val)
        bh.show()


# Show delete key
def example3():
    bh = BinomialHeap()
    a = [i for i in range(16)]
    for i in a:
        bh.insert(i)
    bh.show()
    print("\n------------")
    print("Delete key:", 13)
    print("------------")
    bh.delete_key(6)
    bh.show()

example()