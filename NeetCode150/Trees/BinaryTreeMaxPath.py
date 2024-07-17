""" 
Hard: Given a binary tree, return the maximum path sum of any non-empty path.

Sol:
    - We do a dfs inorder traversal, returning the max path of the left and right sides back to the current node at each point.
    - From here we can calculate the max path for a given node.
    - We then pass the new max path up to the parent node, either 0, node.val + left, or node.val + right
    
"""

class TreeNode():

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left 
        self.right = right 


def maxPathSum(root):
    maxPath = root.val

    def dfs(root):
        nonlocal maxPath
        if not root:
            return 0 
        left = dfs(root.left)
        right = dfs(root.right)
        new_path = root.val + left + right 
        maxPath = max(maxPath, new_path)
        return max(0, root.val + left, root.val + right)
    
    dfs(root)
    return maxPath


# def maxPathSum(root):
#     res = [root.val]

#     def dfs(root):
#         if not root:
#             return 0
        
#         left = dfs(root.left)
#         right = dfs(root.right)

#         maxLeft = max(0, left)
#         maxRight = max(0, right)

#         res[0] = max(res[0], root.val + left + right)

#         return root.val + max(maxLeft, maxRight)
    
#     dfs(root)

#     return res[0]
