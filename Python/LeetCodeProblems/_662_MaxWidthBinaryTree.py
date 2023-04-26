"""
Given a Binary Tree's root node, return the maxi width of said tree.

Intuition:
    - We know some important facts about binary trees that can be useful here.
    - The leftmost node on a level is at index (2^l - 1)
    - The rightmost node on a level is at index (2^l+1 - 2)
    - For a given node with index i, its left child has index 2i+1 and its right has index 2i+2
    - Given node with index i, its parent node has index (i-1)/2

Solution:
    - Now we can traverse the tree through each level using a BFS, we simply need to keep track of the indices of each
    node, and this allows us to quickly compute the width at each level

"""


class Node:

    def __init__(self):
        self.val = None
        self.left = None
        self.right = None


def find_max_width(root):
    if not isinstance(root, Node):
        return
    nodes = [(root, 0)]
    m_width = 1
    while nodes:
        children = []
        for node in nodes:
            if node[0].left:
                children.append((node[0].left, 2*node[1] + 1))
            if node[0].right:
                children.append((node[0].right, 2 * node[1] + 2))
        if children:
            width = children[-1][1] - children[0][1] + 1
            if width > m_width:
                m_width = width
        nodes = children
    return m_width

