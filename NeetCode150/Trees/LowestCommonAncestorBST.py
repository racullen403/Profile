"""
Medium: Given a BST (Binary Search Tree), where node values are unique, and two nodes p and q, return the LCA (lowest common ancestor) of the 2 nodes.
The LCA is if nodes p and q is the lowest node of the tree such that p and q are both descendents. Note that an ancestor can be the descendent (p or q).
Note p and q will always exists in the tree.

Sol:
    - Ensure p < q by swapping if needed.
    - Traverse the BST either left if both p and q are to the left, or right if both p and q are to the right.
    - Since we know p and q always exist, if the above are not met, then we are at the LCA (ie p left and q right, or we are at p or we are at q).
    
"""
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val 
        self.left = left
        self.right = right 


def lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    temp = root
    if p.val > q.val:
        p, q = q, p
    while temp:
        val = temp.val 
        if p.val < val and q.val < val:
            temp = temp.left
        elif p.val > val and q.val > val:
            temp = temp.right 
        else:
            return temp
        