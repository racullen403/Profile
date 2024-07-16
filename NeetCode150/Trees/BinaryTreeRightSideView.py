""" 
Medium: Given a Binary Tree, return the values of nodes that are only viewable from the right, ordered top to bottom.

Sol:
    - BFS and simply add the last node in queue at each level to a list.
"""
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val 
        self.left = left
        self.right = right 

def rightSideView(root):
    res = []
    if not root:
        return res
    queue = [root]
    while queue:
        res.append(queue[-1].val)
        new_queue = [] 
        for node in queue:
            if node.left:
                new_queue.append(node.left)
            if node.right:
                new_queue.append(node.right)
        queue = new_queue
    return res

