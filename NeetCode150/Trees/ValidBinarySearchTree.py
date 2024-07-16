"""  
Medium: Given a binary tree, return true/false if it is valid. 
    
    Valid if: 
        - all nodes in left subtree contain keys smaller than root
        - all nodes in right subtree contain keys larger than root
        - both left and right subtrees ar also a BST

Sol:
    - We do a DFS storing the values for left and right that the current node must lie between.
    - If we step left, then new nodes right value is its parent node value.
    - If we step right, then new nodes left value is its parent value.
    - Simply ensure node value lies between these values at each stage.
"""
class TreeNode():

    def __init__(self, val=0, left=None, right=None):
        self.val = val 
        self.left = left 
        self.right = right 


def isValidBST(root):
    
    def dfs(node, left, right):
        if not node:
            return True 
        if not (left < node.val < right):
            return False 
        return dfs(node.left, left, node.val) and dfs(node.right, node.val, right)
    
    return dfs(root, float("-inf"), float("inf"))
