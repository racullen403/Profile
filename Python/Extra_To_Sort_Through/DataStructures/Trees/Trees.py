"""
We can represent a tree data structure either using a list and its indexing (for Complete trees) or
by using a Node class that points to its child subtrees (linked list like structure / Graph).

Terminology:
    - Node is an entity containing data on a specific key, and pointers to its child nodes/subtrees.

    - Leaf is the last/outer nodes of a tree, its child pointers are None.

    - An internal Node is any node containing at least _01_BasicPython child node.

    - Edge is just the link between two nodes (commonly used in graphs).

    - Root is the top node of the tree.

    - Height of a tree/subtree is how many edges to the furthest leaf.

    - Depth of a node is the number of edges to said node from the root.

    - Degree of a node is the number of children it has.

    - Forest is a collection of trees (usually roots form a linked-list or just stored in a
    list structure).

Traversal:
    - To perform an operation on a node, we first have to search a tree to find the node, this
    is referred to as tree traversal.
    - We have different ways to traverse a tree:

        Inorder:    Left subtree -> Check node -> Right subtree
        Preorder:   Check node -> Left subtree -> Right subtree
        Postorder:  Left subtree -> Right subtree -> Check node

        eg.             _01_BasicPython
                    2       3
                 4     5  6   7

        Inorder:    4 2 5 _01_BasicPython 6 3 7
        Preorder:   _01_BasicPython 2 4 5 3 6 7
        Postorder:  4 5 2 6 7 3 _01_BasicPython

Note following methods are for Complete Binary trees
"""


# Using indexing
def inorder(arr, ind):
    if ind < len(arr):
        inorder(arr, 2*ind + 1)
        print(arr[ind], end=" -> ")
        inorder(arr, 2*ind + 2)
    return


# Using indexing
def preorder(arr, ind):
    if ind < len(arr):
        print(arr[ind], end=" -> ")
        preorder(arr, 2*ind + 1)
        preorder(arr, 2*ind + 2)
    return


# Using indexing
def postorder(arr, ind):
    if ind < len(arr):
        postorder(arr, ind*2 + 1)
        postorder(arr, ind*2 + 2)
        print(arr[ind], end=" -> ")
    return


tree = [1, 2, 3, 4, 5, 6, 7]
print("----Inorder----")
inorder(tree, 0)
print("\n----End----")
print("\n----Preorder----")
preorder(tree, 0)
print("\n----End----")
print("\n----Postorder----")
postorder(tree, 0)
print("\n----End----")


""" 
Example using Node Class for tree structure (Binary tree)
"""


class Node(object):

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def inorder_node(node):
    if node is not None:
        inorder_node(node.left)
        print(node.data, end=" -> ")
        inorder_node(node.right)
    return

# Create the tree using this class
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

# inorder traverse the tree "root"
print("\n----Inorder on Node----")
inorder_node(root)
print("\n----End----")

