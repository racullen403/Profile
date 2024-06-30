"""
Given a Binary Tree, we must return the tree inverted left ro right.

Solution 1:
    - This is simply a matter of swapping left and right child nodes in the correct order. This can be done recursively
    using a DFS

Solution 2:
    - If we want to avoid recursion, we can use a stack to iteratively swap the child nodes and retain correct order
    of swaps needed.

        e.g         1
                   / \
                  2   3
                 /\   /\
                4  5 6  7

                we start with stack=[1], pop 1 out, swap its kids, then add the kids into the stack left to right

                Now, stack=[3, 2] and tree looks like

                     1
                   / \
                  3   2
                 /\   /\
                6  7 4  5

                Simply repeat the process until the stack is empty.

    - We can see that by using the stack, we keep the same order as the DFS method, ie swap child nodes, visit right...
    until we reach the end of the right path, then is visits the closest left and repeats, a DFS.

    


"""


class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def invertBinaryTree(root):
    if not root:
        return None
    temp = root.left
    root.left = invertBinaryTree(root.right)
    root.right = invertBinaryTree(temp)
    return root


def invertBTstack(root)
    if root:
        stack = [root]
        while stack:
            n = stack.pop()
            n.left, n.right = n.right, n.left
            if n.left:
                stack.append(n.left)
            if n.right:
                stack.append(n.right)
    return root