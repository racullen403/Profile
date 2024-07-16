""" 
Medium: Given binary tree root, return tje level order traversal of it as a nested list, where each sublist contains the values of the 
nodes at a given level from left to right.

Sol:
    - Sounds like a BFS, append values into lists for each level and create new queue of child nodes
"""
class TreeNode:

    def __init__(self, val=0, left=None, right=None):
        self.val = val 
        self.left = left
        self.right = right 


def levelOrderTraversal(root):
    res = [] 
    if not root:
        return res
    queue = [root]
    while queue:
        new_queue = []
        level = []
        for i in range(len(queue)):
            node = queue[i]
            level.append(node.val)
            if node.left:
                new_queue.append(node.left)
            if node.right:
                new_queue.append(node.right)
        res.append(level)
        queue = new_queue
    return res