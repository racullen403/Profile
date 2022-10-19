"""
Tree Data Structure:

    Unlike the array, linked list, queue, stack etc... which are all linear structures (we must traverse them
    sequentially, one by one), the tree structure forms a hierarchy of levels, that are structured in such a way as
    to allow us to traverse them logarithmically (usually).

    Basic Structure:
        - Data is stored in a Node, which will have pointers to children, parents, siblings, all dependent on how we
         want to structure it.
        - Nodes simply point to other Nodes which collectively form the tree.
        - The "Root" node is the head/top of the tree, it is the first node in the traversal.
        - Leaf-Nodes are the very end nodes in a tree, their children pointers will be NONE.
        - We call the connecting pointer an "Edge", this is a term used for "graph" structures.

    The height of a node is given by the length of the path (number of edges) from the node to its deepest Leaf-Node.

    The depth of a node is the number of edges from the Root to said Node.

    The Degree of a node is the Number of "Branches" of the node, ie 2 children would be degree 2.

    A Forest is just a collection of Trees, we can store this as a linked list of Root Nodes.


Binary Trees:
    A Binary Tree is just a tree structure where each node can have at most 2 child nodes.

    Types:
        - Full (Proper), every node has 2 children minimum (except leaf nodes, with 0 children)
        - Perfect, every internal node has 2 child nodes, and every leaf node is on the same level (at same depth)
        - Complete, every depth level is filled except the last, which is filled from the left.
        - Degenerate, a tree where nodes only have one left or right child
        - Skewed, a degenerate tree dominated by either left children or right children.
        - Balanced, a tree in which at every node, the difference in height between the left and right child is 0 or 1.

    Full Binary Trees:
        - Let n be the number of nodes
        - Number of Internal Nodes is (n-1)/2
        - Number of leaf nodes is (n+1)/2

    Perfect Binary Trees:
        - We can define it recursively as follows:
            - Leaf node is a perfect binary tree of height 0
            - A node of height h is a perfect binary tree if both its subtrees are of height h-1 and perfect
            binary trees.

    Complete Binary Tree:
        - We can represent this in an array using indexes:
                - For some node given by index i, its left child will be at (2i+1) and its right child will be
                at (2i+2)
                - Parent node is given by (i-1)/2


Traversal:

    - Inorder, visits left subtree's first, then root nodes, then right subtree's.

    - Preorder, visits the root node first, then left subtree, the right subtree.

    - Postorder, visits the right subtree's first, the root nodes, the left subtrees

We will create a Binary Search Tree as an example below, and show the different Traversal methods.

"""


# Node in a Binary Tree
class Node:

    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None


# Binary Search Tree
class BST:

    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root is None

    def insert(self, val):
        if self.is_empty():
            self.root = Node(val)
        else:
            temp = self.root
            while temp:
                if val <= temp.val:
                    if not temp.left:
                        temp.left = Node(val)
                        temp = temp.left
                    temp = temp.left
                else:
                    if not temp.right:
                        temp.right = Node(val)
                        temp = temp.right
                    temp = temp.right

    def create_tree_from_list(self, arr):
        for obj in arr:
            self.insert(obj)

    def show_tree(self):
        if self.is_empty():
            raise ValueError("Tree is empty")
        else:
            self.show_tree_helper(self.root, "Root:", l=0, root=True)

    def show_tree_helper(self, node, point, l=0, root=False):
        l_spacer = "|     "
        if root:
            print("Root:", end="")
            l = -1
        else:
            print("     " + (l_spacer * l) + point, end="")
        if not node:
            print("NONE")
        else:
            print(node.val)
            self.show_tree_helper(node.left, "|---> L:", l + 1, False)
            self.show_tree_helper(node.right, "|---> R:", l + 1, False)

    def show_order(self, order):
        if self.is_empty():
            raise ValueError("Tree is empty")
        orders = ["inorder", "preorder", "postorder"]
        if order not in orders:
            raise ValueError("Must choose order from: inorder, preorder, postorder")
        print("\n\nTraversal:", order)
        if order == orders[0]:
            self.inorder(self.root)
            print()
        elif order == orders[1]:
            self.preorder(self.root)
            print()
        else:
            self.postorder(self.root)
            print()

    def inorder(self, node):
        if node:
            self.inorder(node.left)
            print(node.val, end=" -> ")
            self.inorder(node.right)

    def preorder(self, node):
        if node:
            print(node.val, end=" -> ")
            self.preorder(node.left)
            self.preorder(node.right)

    def postorder(self, node):
        if node:
            self.postorder(node.left)
            self.postorder(node.right)
            print(node.val, end=" -> ")


# Show all the traversal types
def example1():
    a = [6, 5, 7, 3, 8, 10, 9]
    bst = BST()
    bst.create_tree_from_list(a)
    traverse = ["inorder", "preorder", "postorder"]
    bst.show_tree()
    for t in traverse:
        bst.show_order(t)
