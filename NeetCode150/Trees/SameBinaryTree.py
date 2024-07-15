"""
Easy: Given 2 binary trees p and q, return true/false if they are equivalent (exact same structure and same node values).

Sol:
    - Very similar recursive DFS as before, we just need to compare values this time instead of depths.
"""

class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val 
        self.left = left
        self.right = right 


def isSameTree(p, q):

    def dfs(n1, n2):
        if not n1 and not n2:   # Reach leaf node at same time
            return True 
        elif not n1:            # Structure not the same
            return False
        elif not n2:            # Structure not the same
            return False 
        else:
            # Structure the same so compare values and test next subtrees
            return n1.val == n2.val and dfs(n1.left, n2.left) and dfs(n1.right, n2.right)
        
    return dfs(p, q)
        

        