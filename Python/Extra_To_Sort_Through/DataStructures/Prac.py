import sys

class Node:
    def __init__(self, value):
        self.value = value
        self. parent = None
        self.left = None
        self.right = None
        self.color = 1


class RBTree:
    def __init__(self):
        self.null = Node(0)  # Create a null object that will represent the boundries of the tree, that way we can point back to leaves when needed
        self.null.color = 0  # its color is black
        self.root = self.null  # Root is null to start

    def insert(self, value):
        if self.root is self.null:
            node = Node(value)
            node.color = 0
            node.left = self.null
            node.right = self.null
            node.parent = self.null
            self.root = node
        else:
            node = self.root
            parent = node.parent
            while node != self.null:
                parent = node
                if value <= node.value:
                    node = node.left
                else:
                    node = node.right
            node = Node(value)
            node.left = self.null
            node.right = self.null
            node.parent = parent
            if value <= parent.value:
                parent.left = node
            else:
                parent.right = node
            self.fix_insertion(node)

    def fix_insertion(self, node):
        while node != self.root and node.parent.color == 1:
            if node.parent == node.parent.parent.left:
                uncle = node.parent.parent.right
                if uncle.color == 1:
                    node.parent.color = 0
                    uncle.color = 0
                    node.parent.parent.color = 1
                    node = node.parent.parent
                elif node == node.parent.right:
                    node = node.parent
                    self.left_rotate(node)
                else:
                    node.parent.color = 0
                    node.parent.parent.color = 1
                    self.right_rotate(node.parent.parent)
            else:
                uncle = node.parent.parent.left
                if uncle.color == 1:
                    uncle.color = 0
                    node.parent.color = 0
                    node.parent.parent.color = 1
                    node = node.parent.parent
                elif node == node.parent.left:
                    node = node.parent
                    self.right_rotate(node)
                else:
                    node.parent.color = 0
                    node.parent.parent.color = 1
                    self.left_rotate(node.parent.parent)
        self.root.color = 0

    def delete(self, value):
        node = self.root
        while node.value != value:
            if node == self.null:
                return "Could not find value to delete"
            elif value < node.value:
                node = node.left
            else:
                node = node.right
        d = node
        dc = d.color
        if node.left == self.null:
            r = node.right
            self.transplant(node, node.right)
        elif node.right == self.null:
            r = node.left
            self.transplant(node, node.left)
        else:
            d = self.successor(node.right)
            dc = d.color
            r = d.right
            self.transplant(d, d.right)
            d.right = node.right
            d.right.parent = d
            d.left = node.left
            d.left.parent = d
            d.color = node.color
            self.transplant(node, d)
        if dc == 0:
            self.fix_deletion(r)

    def fix_deletion(self, node):
        while node.color == 0 and node != self.root:
            if node == node.parent.left:
                sib = node.parent.right
                # Case _01_BasicPython -> 2/3/4
                if sib.color == 1:
                    sib.color = 0
                    node.parent.color = 1
                    self.left_rotate(node.parent)
                    sib = node.parent.right
                # Case 2 -> start
                if sib.left.color == 0 and sib.right.color == 0:
                    sib.color = 1
                    node = node.parent
                else:
                    # Case 3 -> 4
                    if sib.right.color == 0:
                        sib.left.color = 0
                        sib.color = 1
                        self.right_rotate(sib)
                        sib = node.parent.right
                    # Case 4 End
                    sib.color = node.parent.color
                    node.parent.color = 0
                    sib.right.color = 0
                    self.left_rotate(node.parent)
                    node = self.root
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

    def successor(self, node):
        while node.left != self.null:
            node = node.left
        return node

    def transplant(self, node, replacement):
        if node is self.root:
            self.root = replacement
        elif node == node.parent.left:
            node.parent.left = replacement
        else:
            node.parent.right = replacement
        replacement.parent = node.parent

    def right_rotate(self, node):
        x = node.left
        b = x.right
        node.left = b
        b.parent = node
        x.parent = node.parent
        if node is self.root:
            x.parent = self.null
            self.root = x
        elif node == node.parent.left:
            node.parent.left = x
        else:
            node.parent.right = x
        node.parent = x
        x.right = node

    def left_rotate(self, node):
        x = node.right
        b = x.left
        node.right = b
        b.parent = node
        x.parent = node.parent
        if node is self.root:
            x.parent = self.null
            self.root = x
        elif node == node.parent.left:
            node.parent.left = x
        else:
            node.parent.right = x
        node.parent = x
        x.left = node

    def show_tree(self, root, indent="", right=True):
        if root is not self.null:
            sys.stdout.write(indent)
            if right is True:
                sys.stdout.write("R--->")
                indent += "     "
            else:
                sys.stdout.write("L--->")
                indent += "|    "
            print(root.value, root.color)
            self.show_tree(root.left, indent, False)
            self.show_tree(root.right, indent, True)

tree = RBTree()
a = [6, 3, 8, 1, 4, 7, 9]
for i in a:
    tree.insert(i)
tree.show_tree(tree.root)
tree.delete(6)
tree.delete(7)
tree.show_tree(tree.root)