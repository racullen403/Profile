"""
Easy: Given binary tree, root, find its depth (longest path from root to leaf)

Sol:
    - Recursively explore the tree and add 1 for each level, maintaining the max value
    - Or use a stack and DFS method to go down the tree, storing the depth and node.
    - Or use a queue and BFS method, simply tracking nodes andf level we are at.
"""
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxDepth(root):
    if not root:
        return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))


# DFS with a stack
def maxDepth2(root):
    stack = [[root, 1]]
    res = 0
    while stack:
        node, depth = stack.pop()
        if node:
            stack.append([node.left, depth + 1])
            stack.append([node.right, depth + 1])
            res = max(res, depth)
    return res


# BFS with a queue
def maxDepth3(root):
    if not root:
        return 0
    queue = [root]
    res = 0 
    while queue:
        new_queue = []
        for q in queue:
            if q.left:
                new_queue.append(q.left)
            if q.right:
                new_queue.append(q.right)
        res += 1
        queue = new_queue
    return res
