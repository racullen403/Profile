""" 
Medium: Given a BST and and integer k, find the kth smallest value in the tree

Sol:
    - Do a DFS with conditions to always search left, then current, then right nodes, this ensures we are trying to find the smallest.
    - Once we reach None, we will return to the smallest node, from here we keep a count.
    - Each time we return, count increases by 1.
    - Once count is the same as k, we are at the right node.
"""

class TreeNode():

    def __init__(self, val=0, left=None, right=None):
        self.val = val 
        self.left = left 
        self.right = right 


def kthSmallest(root, k):
    
    smallest = root
    res = 0

    def dfs(node):
        nonlocal smallest
        nonlocal res
        if not node:
            return 0 
        dfs(node.left)
        res += 1
        if res == k:
            smallest = node
        dfs(node.right)
        return res
    

    # stack = []
    # temp = root 
    # count = 0
    # while stack or temp:
    #     while temp:
    #         stack.append(temp)
    #         temp = temp.left
    #     node = stack.pop()
    #     count += 1
    #     if count == k:
    #         return node.val 
    #     if node.right:
    #         temp = node.right
    # return
        

    
    dfs(root)

    return smallest.val

