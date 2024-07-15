"""
Easy: Diameter of binary tree is the distance of the longest path between any two nodes.

Sol:
    - Simply do a dfs to find the depth recursively, but store the depth in left and right variables so we can compare the path.
    - At each node compare the longest path ie left+right depth to the current result
"""
class TreeNode():

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left 
        self.right = right 


def diameterOfBinaryTree(root):
    res = 0
       
    def depth(node):
        nonlocal res
        if not node:
            return 0
        left = depth(node.left)
        right = depth(node.right)
        res = max(res, left + right) 
        return 1 + max(left, right)
    
    depth(root)
    
    return res