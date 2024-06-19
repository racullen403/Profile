"""
Binary Search Tree:

    This is a tree structure  has the following properties:
        - All nodes in the left subtree less than the root node
        - All nodes in the right subtree are greater than the root node
        - Both subtrees are also BST, obeying the above

    This structuring gives the BST a logarithmic search time (in general, skewed trees may become linear due to
    the one side being weighted, this can be corrected using self-balancing).


    Searching:
        This is just a matter of moving down the left subtree if value we are looking for is less than current
        value, or down the right if it is greater.


    Insertion:
        - This is similar to searching, going down left or right subtrees until we find an open position.
        - This will happen when we reach a None value that a node has pointed to, place the new Node(val) here.


    Deletion:
        - Slightly more complicated, the obvious case is when we search down the tree and find our value and it either
        has 1 or 0 child nodes. With 0 children we just make the parent node point to None, with 1 child, we make
        the parent point to the nodes only child (in this way we are skipping the node, effectively deleting it).
        - The more complicate case is when the node found containing value has 2 children. In this case we must replace
        it with the inorder successor (the next smallest value in the right subtree), and then continue down the right
        subtree to now delete the inorder successor value.


In general these are all O(logn) time complexity.

We can make these operations O(1) space complexity by avoiding using recursion, and simply using pointers to travel
down the tree. If we are using recursion, we would need to retain one node at each leveling in the stack, taking O(d)
where d is the depth of the final node (average case is O(logn)).
"""


class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    # Non-recursive approach to insertion
    def insert(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            temp = self.root
            while temp:
                if val <= temp.val:
                    if temp.left is None:
                        temp.left = Node(val)
                        temp = temp.left
                    temp = temp.left
                else:
                    if temp.right is None:
                        temp.right = Node(val)
                        temp = temp.right
                    temp = temp.right

    # Recursive approach to insertion
    def insert_r(self, val):
        def insert_recursive(node):
            if node is None:
                return Node(val)
            else:
                if val <= node.val:
                    node.left = insert_recursive(node.left)
                else:
                    node.right = insert_recursive(node.right)
            return node
        self.root = insert_recursive(self.root)

    def create_tree_from_list(self, arr):
        for obj in arr:
            self.insert(obj)

    def show(self):
        def show_tree(node, count, left):
            if node:
                spacer = "|     "
                if node is not self.root:
                    print("     ", end="")
                print((spacer * count), end="")
                if node is self.root:
                    print("Root:", end="")
                    count = -1
                elif left:
                    print("|---> L:", end="")
                else:
                    print("|---> R:", end="")
                if node:
                    print(node.val)
                    show_tree(node.left, count + 1, True)
                    show_tree(node.right, count + 1, False)
                else:
                    print("NONE")
        if self.root is None:
            return
        show_tree(self.root, 0, True)

    def find(self, val):
        if self.root is None:
            return
        else:
            temp = self.root
            while temp:
                if temp.val == val:
                    return temp
                elif val < temp.val:
                    temp = temp.left
                else:
                    temp = temp.right
            return None

    # Non-Recursive approach, tracks both temp node and parent node
    def delete(self, val):
        if self.root is None:
            return
        parent = None
        temp = self.root
        while temp:
            if val < temp.val:
                parent = temp
                temp = temp.left
            elif val > temp.val:
                parent = temp
                temp = temp.right
            else:  # We have found val at temp
                if temp.left and temp.right:  # Left and right child exist, we replace node val with inorder successor
                    inorder = self.inorder_successor_helper(temp).val
                    temp.val = inorder
                    val = inorder
                    parent = temp
                    temp = temp.right  # Continue as before but now delete inorder successor
                else:  # Case when only 1 or 0 children
                    if temp.left:
                        successor = temp.left
                    else:
                        successor = temp.right  # Successor gives next node we will make parent node point to
                    if parent is None:
                        self.root = successor
                    elif parent.left == temp:
                        parent.left = successor
                    else:
                        parent.right = successor
                    temp = successor
        return

    # Recursive approach to deletion
    def delete_r(self, val):
        def delete_recursive(value, node):
            if not node:
                return None
            else:
                if value < node.val:
                    node.left = delete_recursive(value, node.left)
                elif value > node.val:
                    node.right = delete_recursive(value, node.right)
                else:
                    if not node.right:
                        return node.left
                    elif not node.left:
                        return node.right
                    else:
                        node.val = self.inorder_successor_helper(node).val
                        node.right = delete_recursive(node.val, node.right)
            return node
        self.root = delete_recursive(val, self.root)

    def inorder_successor_helper(self, node):
        temp = node.right
        while temp.left:
            temp = temp.left
        return temp

    def preorder_successor_helper(self, node):
        temp = node.left
        while temp.right:
            temp = temp.right
        return temp


def example1():
    from random import shuffle
    a = [*range(10)]
    shuffle(a)
    print("Original Array:", a, "\n")
    bt = BST()
    bt.create_tree_from_list(a)
    bt.show()
    print()
    for i in range(10):
        found = bt.find(i)
        if found is None:
            print("Could not find:", i)
        print("Found", found.val)
    for j in a:
        print("\nDeleting:", j)
        bt.delete(j)
        bt.show()
    print("\n\nRecursive Insert:\n")
    for obj in a:
        bt.insert_r(obj)
    bt.show()
    for j in a:
        print("\nRecursive Deleting:", j)
        bt.delete_r(j)
        bt.show()


example1()

