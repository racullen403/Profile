"""
Binary Tree is a tree data structure where internal nodes have at most 2 children.

Types:
    - Full Binary Tree: when every internal node has 2 children
    - Perfect Binary Tree: when every internal node has 2 children and all leaves are on same level
    - Complete Binary Tree: when every level of the tree is filled except the last, where leaf
    nodes fill from the left (doesn't have to be full).
    - Degenerate tree: when tree only has a single child.
    - Skewed: a degenerate tree dominated by left nodes or right nodes
    - Balanced: when the height difference between left and right subtrees is 0 or _01_BasicPython

Full Binary Tree:
    - The number of internal node is (n-_01_BasicPython)/2
    - The number of leaves is (n+_01_BasicPython)/2
    - So the number of internal nodes is _01_BasicPython less than the number of leaves
    - The number of leaves is at most (2**levels)-_01_BasicPython

Perfect Binary Tree:
    - When every node has either 2 children or none, this results in every level being filled.
    - If a node has height 0 then it has no children, if its height > 0 then it must have
    2 children

Complete Binary Tree:
    - Tree where all levels are completely filled except the last, where leaves are filled
    from the left
    - We count the number of nodes in the tree, then traverse the tree updating the equivalent
    index position (left child 2*_01_BasicPython + _01_BasicPython ...), if this index points to a node out side the last
    index of a complete tree, it is not a complete tree.

Balanced Binary Tree:
    - A binary tree is balanced if the difference in height of left and right subtrees, at each
    node is 0 or _01_BasicPython.
"""


class Node(object):

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.height = 0

    # Method to display inorder traversal
    def inorder_traverse(self):
        if self.left:
            self.left.inorder_traverse()
        print(self.data, end=" -> ")
        if self.right:
            self.right.inorder_traverse()
        return

    def inorder(self):
        print("\n----Inorder----")
        print("Root:", self.data)
        self.inorder_traverse()
        print("\n----End----")

    # Method to display preorder traversal
    def preorder_traverse(self):
        print(self.data, end=" -> ")
        if self.left:
            self.left.preorder_traverse()
        if self.right:
            self.right.preorder_traverse()
        return

    def preorder(self):
        print("\n----Preorder----")
        print("Root:", self.data)
        self.preorder_traverse()
        print("\n----End----")

    # Method to display postorder traversal
    def postorder_traverse(self):
        if self.left:
            self.left.postorder_traverse()
        if self.right:
            self.right.postorder_traverse()
        print(self.data, end=" -> ")
        return

    def postorder(self):
        print("\n----Postorder----")
        print("Root:", self.data)
        self.postorder_traverse()
        print("\n----End----")

    # method to check if tree is a Full Binary Tree
    def is_full(self):
        if self.left is None and self.right is None:
            return True
        elif self.right is None:
            return False
        elif self.left is None:
            return False
        else:
            return self.left.is_full() and self.right.is_full()

    def is_full_show(self):
        print("\n----Checking if Full Binary Tree----")
        print("Node:", self.data)
        print(self.is_full())
        print("----End----")

    # method to check if tree is a perfect binary tree
    def is_perfect_show(self):
        self.update_heights()
        print("\n----Checking if Perfect Binary Tree----")
        print("Node:", self.data)
        print(self.is_perfect())
        print("----End----")

    def is_perfect(self):
        if self.height == 0 and self.left is None and self.right is None:
            return True
        if self.height > 0:
            if self.left is not None and self.right is not None:
                return self.left.is_perfect() and self.right.is_perfect()
            else:
                return False

    # method to check if a tree is a Complete Binary Tree
    def is_complete(self, no_nodes, ind=0):
        if self is not None and ind >= no_nodes:
            return False
        elif self.left is None and self.right is None:
            return True
        elif self.right is None:
            return self.left.is_complete(no_nodes, ind*2 + 1)
        elif self.left is None:
            return self.right.is_complete(no_nodes, ind*2 + 1)
        else:
            return self.left.is_complete(no_nodes, ind*2 + 1) and \
                self.right.is_complete(no_nodes, ind*2 + 2)

    def is_complete_show(self):
        n = self.node_count()
        print("\n----Checking if Complete Binary Tree----")
        print("Node:", self.data)
        print(self.is_complete(n, 0))
        print("----End----")

    # method to check if tree is balance
    def is_balanced(self):
        if self.left is None and self.right is None:
            return True
        elif self.left is None:
            return self.right.height == 1
        elif self.right is None:
            return self.left.height == 1
        else:
            return abs(self.left.height - self.right.height) <= 1

    def is_balanced_show(self):
        self.update_heights()
        print("\n----Checking if tree is Balanced----")
        print("Node:", self.data)
        print(self.is_balanced())
        print("----End----")

    # helper function to update the heights of nodes in the tree
    def update_heights(self):
        if self.left:
            self.left.update_heights()
        if self.right:
            self.right.update_heights()
        if self.left is None and self.right is None:
            self.height = 0
        elif self.left is None:
            self.height = self.right.height + 1
        elif self.right is None:
            self.height = self.left.height + 1
        else:
            self.height = max(self.left.height, self.right.height) + 1

    # helper to count number of nodes in tree
    def node_count(self):
        if self.left is None and self.right is None:
            return 1
        elif self.left is None:
            return self.right.node_count() + 1
        elif self.right is None:
            return self.left.node_count() + 1
        else:
            return self.left.node_count() + self.right.node_count() + 1

""" 
Example:
    
                    _01_BasicPython
            2               3
        4               5       6
                    7       8
        
        Inorder:    4 2 _01_BasicPython 7 5 8 3 6 
        Preorder:   _01_BasicPython 2 4 3 5 7 8 6
        Postorder:  4 2 7 8 5 6 3 _01_BasicPython
"""
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.right.left = Node(5)
root.right.right = Node(6)
root.right.left.left = Node(7)
root.right.left.right = Node(8)


root.inorder()
root.preorder()
root.postorder()

root.is_full_show()

root.is_perfect_show()

root.right.is_perfect_show()

root.is_complete_show()

root.left.is_complete_show()

root.right.is_complete_show()

root.is_balanced_show()

""" 
New Tree, unbalanced

                    _01_BasicPython
            2               3
        4               5       6
                    7      8
                9
"""

root.right.left.left.left = Node(9)
root.is_balanced_show()

