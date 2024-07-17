""" 
Medium: Given two ineger arrays for the preorder and inorder traversal of a binary tree, recreate the try.

Preorder -> Node
            Node.left
            Node.right 

Inorder ->  node.left
            node
            node.right

Postorder ->    node.right
                node
                node.left

Sol:
    - Preorder gives us the order to attach nodes.
    - Finding the position of said node in the Inorder, allows us to tell which nodes are to its left and which nodes are to the right.
    - We can pass this information down as we build the tree
"""

class TreeNode():

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left 
        self.right = right 

def buildTree(preorder, inorder):
    if not preorder or not inorder:
        return None 
    root = TreeNode(preorder[0])
    index = 0
    for i in range(len(inorder)):
        if inorder[i] == preorder[0]:
            index = i 
    root.left = buildTree(preorder[1: index + 1], inorder[: index])
    root.right = buildTree(preorder[index + 1 : ], inorder[index + 1: ])
    return root

