"""
A type of self-balancing BST where each node contains info on its color, red or black.

Properties:
    - Root: Black
    - Leaf: Black, (we refer to the external None Nodes as being the leaves in this case)
    - Inserted nodes start Red, their children are Black.
    - Depth: For every node, any path from it to any of its descendant leaves has the same
    black-depth (number of black nodes excluding the node itself).

These limitations ensure any simple path from the root to a leaf is not more than twice as long as
any other such path.

We use left and right rotations like in our AVLTree.

Insertion:
    - New node is Red
    - Check if tree now violates red-black properties (its parent being red)
    - Recolor and rotate as needed
    - There are 3 cases:

        Case _01_BasicPython:
            - The nodes uncle is red.
            - Make its parent and uncle black and the grandparent red, move pointer from node
            to its grandparent.

        Case 2:
            - The nodes uncle is black or None and the node is a right child.
            - Left rotate its parent node, move the pointer to the new left child position of
            the nodes new position

        Case 3:
            - The nodes uncle is black or None and the node is a left child.
            - We change the nodes parent color to black, its grandparent to red and then
            right rotate the grandparent.

Deletion:
    - We search for the node to be deleted, Node.
    - Retain its color, deleted_color.
    - If left child is None, save right as X and replace Node with X.
    - Elif right child is None, save left as X and replace Node with X.
    - Else, left and right are not None. Find inorder successor of right subtree, Y, save its
    color in deleted_color and replace Node with the successor, delete successor.
    - If the color of deleted_color is black, then the tree now violates the black depth property. We say the node
    that replaces the deleted node now contains an extra black, represented by having a pointer, x, point to it. We now
    consider the following:

        While x is black and not the root
            If it is a left child then the right child is sib

            Case _01_BasicPython: sib is red
                set sib to black, set parent of x to red, left rotate parent of x, assign the sib of x to its new node

            Case 2: sib is black and both its children are black
                set sib to red, assign x to the parent of x

            Case 3: sib is black and right child is black, (left would be red now)
                set left child to black, set sib to red, right rotate the sib, assign sib of x to its new node

            Case 4: if none of the above cases, (ie sib is black and right child is red)
                set sib to color of parent of x, grand parent of x to black, set right child of w to black,
                left rotate the parent of x and set x  to the root (this ends the loop)

            Else x is a right child and sib will be the left child, simply repeat but for symmetric opposite.
        Finally set the root to black

    - Note this is pretty complicated and is easier with pictures,
    https://www.programiz.com/dsa/deletion-from-a-red-black-tree


"""
import sys


class Node(object):

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None
        self.color = 1  # RED by default, makes life easy


class RBTree(object):

    # initialise a pointer to the root of the tree and a Null node that is black
    def __init__(self):
        self.null = Node(0)
        self.null.color = 0
        self.root = self.null

    # BST insert and then apply our balancing procedure
    def insert_node(self, value):
        # When root is none we create new root node with color black
        if self.root is self.null:
            self.root = Node(value)
            self.root.left = self.null
            self.root.right = self.null
            self.root.parent = self.null
            self.root.color = 0
        else:
            # Create node pointer and parent pointer
            node = self.root
            parent = node.parent
            # Iterate down to node=None, the BST position
            while node != self.null:
                parent = node
                if value <= node.value:
                    node = node.left
                else:
                    node = node.right
            # Insert new node here
            node = Node(value)
            node.left = self.null
            node.right = self.null
            # Assign node its parent, and parent its child (in correct position)
            node.parent = parent
            if node.value <= parent.value:
                parent.left = node
            else:
                parent.right = node
            # Apply our balancing procedure on newly inserted node
            self.fix_insert(node)

    # Method to delete a node from the RBTree.
    def delete_node(self, value):
        # start at root
        node = self.root
        # iterate through until we find the node to be deleted
        while node.value != value:
            if node == self.null:
                return "Could not find node"
            elif value < node.value:
                node = node.left
            else:
                node = node.right
        # d is the current node to be deleted
        d = node
        d_color = d.color
        # If d is missing a left child, then we want to remove d and replace it with its right child
        if node.left == self.null:
            r = node.right
            self.node_replace(node, node.right)
        # If d is missing a right child, then we want to remove d and replace it with its left child
        elif node.right == self.null:
            r = node.left
            self.node_replace(node, node.left)
        # If d has both children, we  want to replace it with its inorder successor, and then remove
        # the old inorder successor node
        else:
            d = self.minimum(node.right)
            r = d.right
            d_color = d.color
            if d.parent == node:
                r.parent = d
            else:
                self.node_replace(d, d.right)
                d.right = node.right
                d.right.parent = d
            self.node_replace(node, d)
            d.left = node.left
            d.left.parent = d
            d.color = node.color
        if d_color == 0:
            # note that replacement node r might be a self.null node, this contains the color black
            # and a pointer to a parent, this is required for fixing the deleted node
            self.fix_delete(r)

    # method to show the tree in a meaningful way, uses inorder recursion with indentation
    def show_tree(self, root, indent="", right=True):
        if root != self.null:
            sys.stdout.write(indent)
            if right:
                sys.stdout.write("R--->")
                indent += "     "
            else:
                sys.stdout.write("L--->")
                indent += "|    "
            print(root.value, str(self.show_color(root)))
            self.show_tree(root.left, indent, False)
            self.show_tree(root.right, indent, True)

    # helper to return correct color
    def show_color(self, node):
        if node.color == 0:
            return "Black"
        else:
            return "Red"

    # helper to replace node with another
    def node_replace(self, node_delete, node_replace):
        node_replace.parent = node_delete.parent
        if node_delete.parent == self.null:
            self.root = node_replace
        elif node_delete == node_delete.parent.left:
            node_delete.parent.left = node_replace
        else:
            node_delete.parent.right = node_replace

    # helper to fix when node is deleted, we want to push the extra black up the tree until we either
    # reach a red, reach the root, or remove through rotations and recoloring
    # node points to the node with the extra black
    def fix_delete(self, node):
        while node != self.root and node.color == 0:
            if node == node.parent.left:
                sib = node.parent.right
                # Case _01_BasicPython, node is left child and right sibling is red, converts into case 2,3 or 4
                if sib.color == 1:
                    sib.color = 0
                    node.parent.color = 1
                    self.left_rotate(node.parent)
                    sib = node.parent.right
                # Case 2, sib is black and both of siblings children are black
                if sib.left.color == 0 and sib.right.color == 0:
                    sib.color = 1
                    node = node.parent
                # Case 3
                else:
                    if sib.right.color == 0:
                        sib.left.color = 0
                        sib.color = 1
                        self.right_rotate(sib)
                        sib = node.parent.right
                    sib.color = node.parent.color
                    node.parent.color = 0
                    sib.right.color = 0
                    self.left_rotate(node.parent)
                    node = self.root
            # all same but symmetrically opposite
            else:
                sib = node.parent.left
                if sib.color == 1:
                    sib.color = 0
                    node.parent.color = 1
                    self.right_rotate(node.parent)
                    sib = node.parent.left
                if sib.left.color == 0 and sib.right.color == 0:
                    sib.color = 1
                    node = node.parent
                else:
                    if sib.left.color == 0:
                        sib.right.color = 0
                        sib.color = 1
                        self.left_rotate(sib)
                        sib = node.parent.left
                    sib.color = node.parent.color
                    node.parent.color = 0
                    sib.left.color = 0
                    self.right_rotate(node.parent)
                    node = self.root
        node.color = 0

    # helper to fix when node is inserted
    def fix_insert(self, node):
        # Repeat so long as nodes parent is red and the node isn't the root
        while node != self.root and node.parent.color == 1:
            # When nodes parent is a left child
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                # Case _01_BasicPython, uncle is red
                if uncle.color == 1:
                    node.parent.color = 0
                    uncle.color = 0
                    node.parent.parent.color = 1
                    # update pointer
                    node = node.parent.parent
                # Uncle doesn't exist, or is black
                else:
                    # Case 2, node is a right child and uncle is black
                    if node == node.parent.right:
                        node = node.parent
                        self.left_rotate(node)
                    # Case 3, always applies after 2, node is left child and uncle is black
                    node.parent.color = 0
                    node.parent.parent.color = 1
                    self.right_rotate(node.parent.parent)
            # The parent node is a right child, all the same but symmetrically opposite
            else:
                uncle = node.parent.parent.left
                if uncle.color == 1:
                    node.parent.color = 0
                    uncle.color = 0
                    node.parent.parent.color = 1
                    node = node.parent.parent
                else:
                    if node == node.parent.left:
                        node = node.parent
                        self.right_rotate(node)
                    node.parent.color = 0
                    node.parent.parent.color = 1
                    self.right_rotate(node.parent.parent)
        # Ensures root is black
        self.root.color = 0

    # helper to left rotate a parent node
    def right_rotate(self, node):
        """
            self.right_rotate(X)

                 X       -->      Y
                / \              / \
               Y   C            A   X
              / \                  / \
             A   B                B   C
        """
        x = node.left
        b = x.right
        node.left = b
        if b != self.null:
            b.parent = node
        x.parent = node.parent
        if node.parent == self.null:
            self.root = x
        elif node == node.parent.left:
            node.parent.left = x
        else:
            node.parent.right = x
        x.right = node
        node.parent = x

    # helper to right rotate a parent node
    def left_rotate(self, node):
        """
            self.left_rotate(Y)

                Y       -->      X
               / \              / \
              A   X            Y   C
                 / \          / \
                B   C        A   B
        """
        x = node.right
        b = x.left
        node.right = b
        if b != self.null:
            b.parent = node
        x.parent = node.parent
        if node.parent == self.null:
            self.root = x
        elif node == node.parent.left:
            node.parent.left = x
        else:
            node.parent.right = x
        node.parent = x
        x.left = node

    # helper to find the inorder successor of a node's right subtree
    def minimum(self, root):
        node = root
        while node.left != self.null:
                node = node.left
        return node


rb = RBTree()
nodes = [6, 3, 8, 1, 4, 7, 9]
for i in nodes:
    rb.insert_node(i)
rb.delete_node(6)
rb.delete_node(7)
rb.show_tree(rb.root)
