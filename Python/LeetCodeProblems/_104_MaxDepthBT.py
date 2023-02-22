"""
Given a Binary Tree, we want to return the maximum depth.

Solution 1:
    - The obvious case is to simply do a DFS of the tree and keep track of the current and maximum depth found, updating
    the maximum depth when necessary.
    - This would need O(1) memory to store the current and maximum depth variables, and O(n) time do the dfs of the
    tree


Solution 2:
    - We can use the optimal substructure of this problem. Clearly the maximum depth of the root node will be 1 + the
    maximum depth of the left and right child nodes, in this way we can build the solution up recursively from the
    bottom up.
    - Note that this solution will apply a DFS recursively without needing to store the depth variables of solution 1

"""


class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# Solution 2
def maxDepth(root):
    if root is None:
        return 0
    return max(maxDepth(root.left), maxDepth(root.right)) + 1
