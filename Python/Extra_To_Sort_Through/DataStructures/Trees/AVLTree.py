"""
AVL tree has logn insertion, deletion and searching.

An AVL tree is a self balancing binary search tree that maintains a balance factor of 0, -_01_BasicPython, +_01_BasicPython
at every node, this is the height difference between left and right subtrees.

The key to this self-balancing is a rotation operation between the nodes:

    Left Rotate:

                       P
                       |
                       X
                     /   \
                    A     Y
                         / \
                        B   C

        We want to make the arrangement of nodes on the right transform into those on the left:
            - Make X the parent of left subtree B
            - If P is None make Y the root
            - Else if X is left child of P make Y left child of P
            - Else make Y right child of P
            - Assign Y as the parent of X


                      P
                      |
                      Y
                    /  \
                   X    C
                  / \
                 A   B

    Right Rotate:

                      P
                      |
                      Y
                    /  \
                   X    C
                  / \
                 A   B

        We want to make the arrangement of nodes on the left transform into those on the right:
            - Make Y the parent of B if it exists
            - If P is Null make X the root
            - Else if Y is the left child of P make X the left child of P
            - Else make X the right child of P
            - Make X the parent of Y


                       P
                       |
                       X
                     /   \
                    A     Y
                         / \
                        B   C


We use a combination of these rotations on the nodes, depending on the balance factor, to
create the balanced tree.

    Left-Right:

             Z
            /
           X
            \
             Y

             Left  rotate x-y

              Z
             /
            Y
           /
          X

          Right rotate y-z

            Y
          /   \
         X     Z


    Right-Left:

        Z
         \
          X
         /
        Y

        Do a right rotation x-y

        Z
         \
          Y
           \
            X

        Do a left rotation z-y

           Y
         /   \
        Z     X

Insertion:
    - New node insert with a balance factor 0
    - Find appropriate insertion point for a BST
    - Update the balance factor of all the node
    - If nodes are unbalanced then re-balance with correct rotations

Balancing:
    - If balance factor > _01_BasicPython, left subtree height is greater than right.
        - If inserted node < parent, do right rotation

            eg     X   Balance = 2      ->       Y          Balance = 0
                  /                            /   \
                 Y                            Node   X
                /
              Node

        - If inserted node > parent, do left-right rotation

            eg     X Balance = 2        ->      X   ->        Node         Balance = 0
                  /                            /            /   \
                 Y                            Node         Y     X
                  \                          /
                  Node                      Y

    - If balance factor < -_01_BasicPython. the right subtree height is greater than the left.
        - If inserted node > parent, do a left rotation

            eg  X  Balance = -2     ->      Y     Balance = 0
                 \                        /   \
                  Y                      X    Node
                   \
                  Node

        - If inserted node < parent, do a right-left rotate

            eg  X  Balance = -2  ->   X         ->      Node          Balance = 0
                 \                     \               /   \
                  Y                     Node           X    Y
                 /                       \
               Node                       Y

Deletion:
    We recursively go down the nodes until we find the node to delete, if its left node is None
    then swap with right node, if its right node is None then swap with left node (this will
    work with leaf nodes also). In the case of a node with two children, we find the inorder
    successor, swap the values of the nodes, then continue the recursion which will delete the new
    leaf node with the swapped value to be deleted.

    We check the balance factor of the nodes when exiting each stage of the recursion.

    If balance factor > _01_BasicPython then left subtree is heavy:

        CASE _01_BasicPython:

            3       --->     3
           / \              /
          2   4            2
         /                /
        _01_BasicPython                _01_BasicPython

        - If the balance factor of root.left (Node(2)) is >=0 we right rotate the root

            2
           / \
          _01_BasicPython   3

        CASE 2:

            3       --->     3
           / \              /
          _01_BasicPython   4            _01_BasicPython
          \                 \
           2                 2

        - If the balance factor of root.left (Node(_01_BasicPython)) is < 0, we left rotate root.left and
        then right rotate the root

    If balance factor < -_01_BasicPython then right subtree is heavy:

        CASE _01_BasicPython:

            3       --->     3
           / \                \
          2   4                4
               \                \
                5                5

        - If the balance factor of root.right (Node(4)) is <=0 we left rotate the root

            4
           / \
          3   5

        CASE 2:

            3       --->     3
           / \                \
          _01_BasicPython   5                5
             /                /
            4                4

        - If the balance factor of root.right (Node(5)) is > 0, we right rotate root.right and
        then left rotate the root

              4
             / \
            3   5

"""
import sys


class Node(object):

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1     # in this case we say a leaf node has height _01_BasicPython instead of 0, makes life easier


class AVLTree(object):

    def __init__(self, node):
        self.root = node

    def avl_insert(self, root, value):
        # recursive insertion of Node in BST position
        if root is None:
            return Node(value)
        elif value <= root.value:
            root.left = self.avl_insert(root.left, value)
        else:
            root.right = self.avl_insert(root.right, value)
        # Need to update heights on way out (inserted will be height _01_BasicPython)
        root.height = self.find_height(root)
        # Need to calc balance factor and rotate when necessary on way out
        balance = self.find_balance(root)
        if balance > 1:
            if value < root.left.value:
                return self.right_rotate(root)
            else:
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)
        if balance < -1:
            if value > root.right.value:
                return self.left_rotate(root)
            else:
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)
        # must return root in order to maintain the nodes of the tree
        return root

    # method to delete a node from the avl tree
    def avl_delete(self, root, value):
        # recursively traverse to the node we want to delete
        if root is None:
            return root
        elif value < root.value:
            root.left = self.avl_delete(root.left, value)
        elif value > root.value:
            root.right = self.avl_delete(root.right, value)
        else:
            # if node is internal with only right child, return the right child in its place
            if root.left is None:
                return root.right
            # if node is internal with only left child, return the left child in its place
            elif root.right is None:
                return root.left
            successor = self.find_successor(root.right)
            root.value = successor.value
            root.right = self.avl_delete(root.right, successor.value)
        # update the heights of nodes on way out of recursion
        root.height = self.find_height(root)
        # update balance and do necessary recursions
        balance = self.find_balance(root)
        if balance > 1:
            if self.find_balance(root.left) >= 0:
                return self.right_rotate(root)
            else:
                root.left = self.left_rotate(root.left)
                return self.right_rotate(root)
        if balance < -1:
            if self.find_balance(root.right) <= 0:
                return self.left_rotate(root)
            else:
                root.right = self.right_rotate(root.right)
                return self.left_rotate(root)
        # return root to maintain the nodes
        return root

    # method to print tree in meaningful way (completely copied it, this is genius)
    def show_tree(self, root, indent, right):
        if root is not None:
            sys.stdout.write(indent)
            if right:
                sys.stdout.write("R--->")
                indent += "     "
            else:
                sys.stdout.write("L--->")
                indent += "|    "
            print(root.value)
            self.show_tree(root.left, indent, False)
            self.show_tree(root.right, indent, True)

    # helper to do left rotate and return higher node
    def left_rotate(self, node):
        y = node.right
        a = y.left
        y.left = node
        node.right = a
        # update heights
        node.height = self.find_height(node)
        y.height = self.find_height(y)
        return y

    # helper to do a right rotate
    def right_rotate(self, node):
        y = node.left
        b = y.right
        y.right = node
        node.left = b
        # update new heights
        node.height = self.find_height(node)
        y.height = self.find_height(y)
        return y

    # helper to find height of node just inserted
    def find_height(self, node):
        if node is None:
            return 0
        else:
            return 1 + max(self.find_height(node.left), self.find_height(node.right))

    # helper to find balance factor of node
    def find_balance(self, node):
        if node is None:
            return 0
        else:
            return self.find_height(node.left) - self.find_height(node.right)

    # helper to find and return the inorder successor node
    def find_successor(self, root):
        if root.left is None and root.right is None:
            return root
        elif root.left:
            return self.find_successor(root.left)
        else:
            return self.find_successor(root.right)

    # method to display avl in preorder
    def avl_preorder(self, root):
        print("Node:", root.value, "Height:", root.height)
        if root.left:
            self.avl_preorder(root.left)
        if root.right:
            self.avl_preorder(root.right)


print("\n----Create AVL with root Node(3)----")
avl = AVLTree(Node(3))
avl.avl_preorder(avl.root)

print("\n----Insert Node(2)----")
avl.root = avl.avl_insert(avl.root, 2)
avl.avl_preorder(avl.root)
avl.show_tree(avl.root, "", True)

""" 
         3
        / 
       2   
"""


print("\n----Insert Node(_01_BasicPython)----")
avl.root = avl.avl_insert(avl.root, 1)
avl.avl_preorder(avl.root)
avl.show_tree(avl.root, "", True)

""" 
         2
        / \
       _01_BasicPython   3
"""

print("\n----Insert Node(0)----")
avl.root = avl.avl_insert(avl.root, 0)
avl.avl_preorder(avl.root)
avl.show_tree(avl.root, "", True)

""" 
         2
        / \
       _01_BasicPython   3
      /
     0
"""

print("\n----Insert Node(-_01_BasicPython)----")
avl.root = avl.avl_insert(avl.root, -1)
avl.avl_preorder(avl.root)
avl.show_tree(avl.root, "", True)

""" 
         2
        / \
       0   3
      / \
    -_01_BasicPython   _01_BasicPython
"""

print("\n----Insert Node(-2)----")
avl.root = avl.avl_insert(avl.root, -2)
avl.avl_preorder(avl.root)
avl.show_tree(avl.root, "", True)
"""    
       0   
      / \
    -_01_BasicPython   2
    /   / \
  -2   _01_BasicPython   3
"""

print("\n----Delete Node(-2)----")
avl.root = avl.avl_delete(avl.root, -2)
avl.avl_preorder(avl.root)
avl.show_tree(avl.root, "", True)
"""    
       0   
      / \
    -_01_BasicPython   2
        / \
       _01_BasicPython   3
"""

print("\n----Delete Node(-_01_BasicPython)----")
avl.root = avl.avl_delete(avl.root, -1)
avl.avl_preorder(avl.root)
avl.show_tree(avl.root, "", True)

"""    
         2
        / \
       0   3
        \
         _01_BasicPython
"""

print("\n----Delete Node(2)----")
avl.root = avl.avl_delete(avl.root, 2)
avl.avl_preorder(avl.root)
avl.show_tree(avl.root, "", True)

"""    
         _01_BasicPython
        / \
       0   3
"""