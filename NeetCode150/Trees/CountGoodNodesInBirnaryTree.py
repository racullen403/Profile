"""
Medium: A node x in a binary tree is good if the path from root to x contains no nodes with values greater than x.

Sol:
    - We need to traverse the tree, storing the current largest value along the path, that way we can compare at node x and see if it is good.
"""
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val 
        self.left = left
        self.right = right 


def goodNodes(root):
    count = 0

    def dfs(node, largest):
        nonlocal count 
        if not node:
            return
        if node.val >= largest:
            count += 1
            largest = node.val
        dfs(node.left, largest)
        dfs(node.right, largest)
        return
    
    # def dfs2(node, largest):
    #     if not node:
    #         return 0
    #     res = 1 if node.val >= largest else 0
    #     largest = max(node.val, largest)
    #     res += dfs(node.left, largest)
    #     res += dfs(node.right, largest)
    #     return res
    
    dfs(root, root.val)

    return count
