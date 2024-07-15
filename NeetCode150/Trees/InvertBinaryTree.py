""" 
Easy: Given a binary tree, invert it and return the root.

Sol:
    - Simply swap left and right children, then apply again on them.
"""
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val 
        self.left = left
        self.right = right 


# Recursive DFS
def invertTree(root):
    if root:
        root.left, root.right = root.right, root.left 
        invertTree(root.left)
        invertTree(root.right)
    return root


    