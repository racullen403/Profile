"""
AVL Tree:

    This is a self-balancing BST where the balance factor at each node is -1, 0, or 1.
        - The balance factor is simply the difference in height of the left and right subtrees.


    The self-balancing is achieved through using Left and Right Node rotations.

        E.G.

            Consider the following nodes

                                       A
                                    /    \
                                  B        C
                                /   \    /   \
                              b1    b2  c1   c2

            In a Left-Rotation, we can think of it as pulling the left subtree, B, downwards, resulting in the right
            subtree, C, being pulled up. We would then attach the left child of C onto the right child of A

                                      C
                                    /   \
                                  A      c2
                                /  \
                              B     c1
                            /   \
                          b1    b2

            In a Right-Rotation, we can think of it as pulling the right subtree, C, downwards, which will then pull
            the left subtree, B, upwards. Finally, attach the right child of B on the left child position of A.

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

        Note, when A becomes unbalanced, b1 and b2 will always be nodes of the same initial height before insertion, or
        else neither will exist and Y would be inserted straight onto B, causing the imbalance. This is simply how a
        balanced tree becomes unbalanced, you will never find a case where b1 and b2 don't have the same initial
        height, yet the tree is unbalanced at A after an insertion into B.


        Case 1: Y was inserted into b1

            We simply do a right rotation between A and B

                                 B
                                / \
                               b1  A
                                  / \
                                 b2  a1

            We reduced the left subtree height by 1 and increased the right subtree height by one, resulting in B
            having balance factor 0.

            We know the height(b2) = height(b1) - 1 and height(a1) = height(b1)-1 and so all nodes are balanced.


        Case 2: Y was inserted into b2

            If we just did a right rotation like above, height(b1) = height(b2) - 1, this would mean the right subtree
            of B above now have a balance factor of -2.

            We correct this by first doing a left rotation between b2 and B in the initial tree.

                                 A
                                / \
                               b2  a1
                              / \
                             B   b2_r
                            / \
                           b1  b2_l

            Now we do the right rotation between b2 and A.

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
        - Deletion occurs in the same way it does in a BST, however, after we remove the node, we must re-balance
        the tree like in insertion

"""


class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 0


class AVL:

    def __init__(self):
        self.root = None

    def insert(self, val):

        def insert_r(node, value):
            if node is None:
                return Node(value)
            else:
                if value <= node.val:
                    node.left = insert_r(node.left, value)
                else:
                    node.right = insert_r(node.right, value)

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

    def get_height_helper(self, node):
        if node is None:
            return -1
        return node.height

    def right_rotate(self, node):
        B = node.left
        b2 = B.right
        node.left = b2
        B.right = node
        node.height = 1 + max(self.get_height_helper(node.left), self.get_height_helper(node.right))  # Must do first
        B.height = 1 + max(self.get_height_helper(B.left), self.get_height_helper(B.right))
        return B

    def left_rotate(self, node):
        B = node.right
        b1 = B.left
        B.left = node
        node.right = b1
        node.height = 1 + max(self.get_height_helper(node.left), self.get_height_helper(node.right))  # Must do first
        B.height = 1 + max(self.get_height_helper(B.left), self.get_height_helper(B.right))
        return B

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


def example1():
    tree = AVL()
    for i in range(10):
        print("\nInserting:", i, "\n")
        tree.insert(i)
        tree.show()


example1()


