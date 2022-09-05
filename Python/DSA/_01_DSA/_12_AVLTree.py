"""
AVL Tree:

    This is a self-balancing BST where the balance factor at each node is -1, 0, or 1.
        - The balance factor is simply the difference in height of the left and right subtrees (we use -1 height if
        a subtree does not exist).

    The self-balancing is achieved through using Left and Right Node rotations.

        E.G.

            Consider the following nodes

                                       A
                                    /    \
                                  B        C
                                /   \    /   \
                              b1    b2  c1   c2

            In a Left-Rotation, we can think of it as pulling the root, A, down to the left, this results in the right
            subtree, C, being pulled up, and placed as the root. We would then attach the left child of C onto the
            right child of A.

                                      C
                                    /   \
                                  A      c2
                                /  \
                              B     c1
                            /   \
                          b1    b2

            In a Right-Rotation, we can think of it as pulling the root, A, downwards to the right, this will then pull
            the left subtree, B, upwards into the root position. Finally, attach the right child of B on the left child
            position of A.

                                      B
                                    /   \
                                   b1    A
                                       /   \
                                      b2    C
                                           /  \
                                          c1  c2


        With these 2 operations, we can ensure the tree always remains balanced.


    Insertion:

        Suppose we start out with some root A, which is balanced, and we add some node Y to the end of its left
        subtree, causing an imbalance in A.

                                 A
                                / \
                               B   a1
                              / \
                             b1  b2

        This will mean the balance factor of A is now +2, and Y was inserted at the end of B's left or right subtrees,
        b1 or b2.

        Note, when A becomes unbalanced after insertion into B, b1 and b2 will always be nodes of the same initial
        height before insertion, or else neither will exist and Y would be inserted straight onto B, causing the
        imbalance. If b1 and b2 where different heights, then insertion into one of them would either unbalance
        B (and A, but we consider B first) or change to balance factor at B back to 0.

        We consider the insertion of Y into subtree B, cause a +2 bf in A.


        Case 1: Y was inserted into b1

            We simply do a right rotation on A

                                 B
                                / \
                               b1  A
                                  / \
                                 b2  a1

            We reduced the left subtree height by 1 and increased the right subtree height by one, resulting in B
            having balance factor 0 at B.

            We know after insertion of Y, the height(b2) = height(b1) - 1 and height(a1) = height(b1)-1 and so
            all nodes are balanced.


        Case 2: Y was inserted into b2

            If we just did a right rotation like above, height(b1) = height(b2) - 1, this would mean the right subtree
            of B in the above case would now have a balance factor of -2.

            We correct this by first doing a left rotation on B in the initial tree.

                                 A
                                / \
                               b2  a1
                              / \
                             B   b2_r
                            / \
                           b1  b2_l

            Now we do the right rotation between on A.

                                     b2
                                /         \
                               B           A
                              / \        /   \
                             b1  b2_l   b2_r   a1

            We know height(a1) = initial height(b2), and initial height(b1) = initial height(b2), now, because Y was
            inserted into b2, we know height(b2_l) = initial height(b2), or height(b2_r) = initial height(b2).
            For whichever b2_l or b2_r that contains the Y node, the other will have height 1 less than it (again
            this is a result of b2_l and b2_r having to be at the same height, otherwise inserting into b2 would have
            caused an imbalance in b2 resulting in it being self balanced and correcting this, causing b2_l and b2_r to
            be on the same level).

            With this, we know the final result is fully balanced.

        We can simply repeat this but do the opposite rotations for a balance factor of -2.


    Deletion:

        Deletion occurs in the same way it does in a BST, however, after we remove the node, we must re-balance
        the tree like in insertion.

            - We only every delete from a leaf node, or an internal node with only 1 child. In all other cases, we
            would find the successor and replace the internal node with it, then continue as before but try to remove
            the successor.


AVL Tree Advantages:
    - Due to near perfect balancing, we can ensure worst case Search operations are still faster than other BST's
    - Insert, Deletion and Search are all O(logn)

AVL Tree Disadvantages:
    - The self-balancing after insertion and deletion can result in many rotations to correct the balance, causing a
    lot of over-head to correct the tree.

AVL Tree Uses:
    - Due to the fast worst case Search and potentially slow worst case insertion and deletion, we want to use an AVL
    tree when we will be doing a lot of searching, and not so much insertion and deletion.
"""


class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
        self.height = 0


class AVL:

    def __init__(self):
        self.root = None

    # Recursive insert
    def insert(self, val):
        def insert_r(node, value):
            if node is None:
                return Node(value)
            else:
                if value <= node.val:
                    node.left = insert_r(node.left, value)
                    node.left.parent = node
                else:
                    node.right = insert_r(node.right, value)
                    node.right.parent = node

                node.height = 1 + max(self.get_height_helper(node.left), self.get_height_helper(node.right))

                balance_factor = self.get_height_helper(node.left) - self.get_height_helper(node.right)

                if balance_factor > 1:
                    if value < node.left.val:  # Case when inserted into b1
                        return self.right_rotate(node)
                    else:
                        node.left = self.left_rotate(node.left)  # Case when inserted into b2
                        return self.right_rotate(node)
                elif balance_factor < -1:
                    if value > node.right.val:
                        return self.left_rotate(node)
                    else:
                        node.right = self.right_rotate(node.right)
                        return self.left_rotate(node)
                return node
        self.root = insert_r(self.root, val)

    # None recursive insert using parent attribute
    def insert_non_recursive(self, val):
        if self.root is None:
            self.root = Node(val)
        else:
            temp = self.root
            inserted = False
            while not inserted:  # Insert Value and end with temp pointing to inserted node
                if val <= temp.val:
                    if not temp.left:
                        temp.left = Node(val)
                        temp.left.parent = temp
                        inserted = True
                    temp = temp.left
                else:
                    if not temp.right:
                        temp.right = Node(val)
                        temp.right.parent = temp
                        inserted = True
                    temp = temp.right
            while temp:  # Correct height and ensure nodes are balanced as we return up the tree to the root
                temp.height = 1 + max(self.get_height_helper(temp.left), self.get_height_helper(temp.right))
                bf = self.get_height_helper(temp.left) - self.get_height_helper(temp.right)
                if bf > 1:
                    if val <= temp.left.val:
                        self.right_rotate(temp)
                    else:
                        self.left_rotate(temp.left)
                        self.right_rotate(temp)
                elif bf < -1:
                    if val > temp.right.val:
                        self.left_rotate(temp)
                    else:
                        self.right_rotate(temp.right)
                        self.left_rotate(temp)
                temp = temp.parent

    def delete(self, val):
        def delete_r(node, value):
            if node is None:
                return node
            else:
                if value < node.val:
                    node.left = delete_r(node.left, value)
                    if node.left:
                        node.left.parent = node
                elif value > node.val:
                    node.right = delete_r(node.right, value)
                    if node.right:
                        node.right.parent = node
                else:
                    if not node.left:
                        return node.right
                    elif not node.right:
                        return node.left
                    else:
                        inorder = self.inorder_successor(node.right)
                        node.val = inorder.val
                        node.right = delete_r(node.right, inorder.val)

                node.height = 1 + max(self.get_height_helper(node.left), self.get_height_helper(node.right))
                balance_factor = self.get_height_helper(node.left) - self.get_height_helper(node.right)

                if balance_factor > 1:
                    if value <= node.left.val:
                        self.right_rotate(node)
                        return node.parent
                    else:
                        self.left_rotate(node.left)
                        self.right_rotate(node)
                        return node.parent
                elif balance_factor < -1:
                    if val > node.right.val:
                        self.left_rotate(node)
                        return node.parent
                    else:
                        self.right_rotate(node.right)
                        self.left_rotate(node)
                        return node.parent
                else:
                    return node
        self.root = delete_r(self.root, val)

    def delete_non_recursive(self, val):
        if not self.root:
            return
        else:
            temp = self.root
            deleted = False
            while temp and not deleted:
                if val < temp.val:
                    temp = temp.left
                elif val > temp.val:
                    temp = temp.right
                else:  # Found val
                    if not temp.right or not temp.left:  # One or None children
                        if temp.right:
                            successor = temp.right
                        else:
                            successor = temp.left
                        if not temp.parent:
                            self.root = successor
                        elif temp == temp.parent.left:
                            temp.parent.left = successor
                        else:
                            temp.parent.right = successor
                        if successor:
                            successor.parent = temp.parent
                        temp = temp.parent
                        deleted = True
                    else:  # Two children
                        successor = self.inorder_successor(temp.right)
                        temp.val = successor.val
                        val = successor.val
                        temp = temp.right
            if not temp:  # Couldn't find val
                return
            else:
                while temp:  # Correct height and ensure nodes are balanced as we return up the tree to the root
                    temp.height = 1 + max(self.get_height_helper(temp.left), self.get_height_helper(temp.right))
                    bf = self.get_height_helper(temp.left) - self.get_height_helper(temp.right)
                    if bf > 1:
                        if val <= temp.left.val:
                            self.right_rotate(temp)
                        else:
                            self.left_rotate(temp.left)
                            self.right_rotate(temp)
                    elif bf < -1:
                        if val > temp.right.val:
                            self.left_rotate(temp)
                        else:
                            self.right_rotate(temp.right)
                            self.left_rotate(temp)
                    temp = temp.parent

    def get_height_helper(self, node):
        if node is None:
            return -1
        return node.height

    def right_rotate(self, node):
        root = node.parent
        B = node.left
        b2 = B.right
        B.right = node
        node.parent = B
        node.left = b2
        if b2:
            b2.parent = node
        if not root:
            self.root = B
        elif node == root.left:
            root.left = B
        else:
            root.right = B
        B.parent = root
        node.height = 1 + max(self.get_height_helper(node.left), self.get_height_helper(node.right))  # Must do first
        B.height = 1 + max(self.get_height_helper(B.left), self.get_height_helper(B.right))
        return B  # Return B for the recursive case

    def left_rotate(self, node):
        root = node.parent
        B = node.right
        b1 = B.left
        B.left = node
        node.parent = B
        node.right = b1
        if b1:
            b1.parent = node
        if not root:
            self.root = B
        elif root.left == node:
            root.left = B
        else:
            root.right = B
        B.parent = root
        node.height = 1 + max(self.get_height_helper(node.left), self.get_height_helper(node.right))  # Must do first
        B.height = 1 + max(self.get_height_helper(B.left), self.get_height_helper(B.right))
        return B  # Return B for the recursive case

    def inorder_successor(self, node):
        while node.left:
            node = node.left
        return node

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


# Example using the recursive insert
def example1():
    tree = AVL()
    for i in range(10):
        print("\nInserting:", i, "\n")
        tree.insert(i)
        tree.show()


# Example using the non-recursive insert
def example2():
    tree = AVL()
    for i in range(10):
        print("\nInserting:", i, "\n")
        tree.insert_non_recursive(i)
        tree.show()


# Example using the non-recursive insert + delete
def example3():
    tree = AVL()
    for i in range(10):
        tree.insert_non_recursive(i)
    print("\n-----Initial Tree-----\n")
    tree.show()
    d = 0
    tree.delete_non_recursive(d)
    print("\n-----Delete {}-----".format(d))
    tree.show()


# Example using the recursive insert + delete
def example4():
    tree = AVL()
    for i in range(10):
        tree.insert(i)
    print("\n-----Initial Tree-----\n")
    tree.show()
    d = 0
    tree.delete(d)
    print("\n-----Delete {}-----".format(d))
    tree.show()

