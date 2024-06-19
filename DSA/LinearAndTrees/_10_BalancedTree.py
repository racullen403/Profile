"""
Balanced Binary Tree:
    A binary tree node is said to be balanced if the difference in height between the left and right subtrees is 0 or
    1. We say the Binary Tree as a whole is balanced if every node in it is balanced.

    We will create the following tree manually:

                         1
                        / \
                       2   3
                      /    / \
                     4    9   8
                    / \
                   7   5
                      /
                     6

        We will then create an algorithm to show if it is balanced, note node (2) has a height difference of 3, and
        so we know the tree is not balanced.


"""


class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class BinaryTree:

    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root is None

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

    # def get_height(self, node):
    #     if not node:
    #         return 0
    #     return 1 + max(self.get_height(node.left), self.get_height(node.right))

    # def is_balanced(self, node):
    #     l = self.get_height(node.left)
    #     r = self.get_height(node.right)
    #     return abs(l - r) < 1 and self.is_balanced(node.left) and self.is_balanced(node.right)

    def is_balanced(self, node):
        """
        We combine the get_height and is_balanced above into one function. Recursively going down left and
        right subtrees, we return the heights and is_balanced in one output list, [height, balanced].
        This way we only have to visit the nodes once and not repeatedly for each get_height call.

            1 + max(l[0], r[0]) gives the height of the node

            abs(l[0] - r[0]) <= 1 and l[1] and r[1] tells us if node is balanced, if at anypoint a node is not
            balanced, it will return up the tree to the final output as False.
        """
        if not node:
            return [0, True]
        l = self.is_balanced(node.left)
        r = self.is_balanced(node.right)
        output = [1 + max(l[0], r[0]), abs(l[0] - r[0]) <= 1 and l[1] and r[1]]
        if node is self.root:
            return output[1]
        return output
    


# Unbalanced Tree
def example1():
    bt = BinaryTree()
    bt.root = Node(1)
    bt.root.left, bt.root.right = Node(2), Node(3)
    bt.root.left.left = Node(4)
    bt.root.left.left.left, bt.root.left.left.right = Node(7), Node(5)
    bt.root.left.left.right.left = Node(6)
    bt.root.right.left, bt.root.right.right = Node(9), Node(8)
    bt.show_tree()
    print("Is balanced:", bt.is_balanced(bt.root))


# Balancing Example:
def example2():
    bt = BinaryTree()
    bt.root = Node(1)
    bt.show_tree()
    print(bt.is_balanced(bt.root), "\n\n")
    bt.root.left, bt.root.right = Node(2), Node(3)
    bt.show_tree()
    print(bt.is_balanced(bt.root), "\n\n")
    bt.root.left.left = Node(4)
    bt.root.left.left.left = Node(5)
    bt.show_tree()
    print(bt.is_balanced(bt.root), "\n\n")
    bt.root.right.right = Node(6)
    bt.show_tree()
    print(bt.is_balanced(bt.root), "\n\n")
    bt.root.left.right = Node(7)
    bt.show_tree()
    print(bt.is_balanced(bt.root), "\n\n")

