"""
Given a Binary Search Tree, find the minimum distance between any 2 nodes.

Solution:
    Given some root node, we know that the minimum distance from said node will be its inorder successor or
    predecessor. Hence, we can traverse the tree "inorder" and simply find the distances between each node.

    We can do this recursively, or check the Morris Traversal / Threaded Binary Tree for traversal inplace.

"""


class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def findMinDistance(root):
    inorder = []

    def inorderTraverse(root):
        if root:
            inorderTraverse(root.left)
            inorder.append(root.val)
            inorderTraverse(root.right)

    inorderTraverse(root)
    min_dist = float("inf")

    for i in range(1, len(inorder)):
        min_dist = min(min_dist, abs(inorder[i] - inorder[i - 1]))

    return min_dist
