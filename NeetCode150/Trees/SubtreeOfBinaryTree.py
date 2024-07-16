""" 
Easy: Given 2 binary trees, return true/false if subRoot is a subtree of root

Sol:
    - We just use our Same Binary Tree solution to make the comparison, and then recursively call this as a helper function as we dfs through root.
"""

class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val 
        self.left = left
        self.right = right 


def isSubtree(root, subRoot):

    def sameTree(p, q):
        if not p and not q:
            return True
        if p and q and p.val == q.val:
            return sameTree(p.left, q.left) and sameTree(p.right, q.right) 
        return False
    
    if not subRoot:
        return True
    if not root:
        return False
    if sameTree(root, subRoot):
        return True
    else:
        return isSubtree(root.left, subRoot) or isSubtree(root.right, subRoot)

    
        
        