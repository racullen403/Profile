"""
Easy: Given binary tree root, return true/false if it is balanced. It is balanced if the difference in left and right subtree depth is no more than 1.

Sol:
    - Again a basic dfs of the nodes keeping track of left and right depth, then compare and check absolute values.
    - If they are >1 then return False.
"""

class TreeNode():

    def __init__(self, val=0, left=None, right=None):
        self.val = val 
        self.left = left 
        self.right = right 


def isBalanced(root):
    res = True

    def depth(node):
        nonlocal res
        if not node:
            return 0 
        left = depth(node.left)
        right = depth(node.right)
        diff = abs (left - right)
        if diff > 1:
            res = False 
        return 1 + max(left, right)
    
    depth(root)

    return res
