class Node:

    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None


class BST:

    def __init__(self, head=None):
        """
        Head should be a Node() that is the start of the tree.
        We can leave as None and use the insert method to add Nodes/vals one at a time, or use the build method to
        construct the tree from a list
        """
        self.head = head

    def insert(self, val):
        """
        Method to insert val to BST
        """
        if self.head is None:
            self.head = Node(val)
        else:
            self.insert_node(val, self.head)

    def insert_node(self, val, node):
        """
        Helper to add Node(val) onto stated node.
        """
        if node is None:
            return Node(val)
        if val <= node.val:
            node.left = self.insert_node(val, node.left)
        else:
            node.right = self.insert_node(val, node.right)
        return node

    def build_bst(self, vals):
        """
        Method to build a BST from a list of values, vals.
        """
        if len(vals) < 1:
            return
        self.head = Node(vals[0])
        if len(vals) > 1:
            for i in range(1, len(vals)):
                self.insert(vals[i])

    def search(self, val):
        """
        Method to search the full tree for val, returns True/False
        """
        return self.search_node(self.head, val)

    def search_node(self, node, val):
        """
        Method to search a node and its branches for val, returns True/False
        """
        if node is None:
            return False
        if node.val > val:
            return self.search_node(node.left, val)
        elif node.val < val:
            return self.search_node(node.right, val)
        else:
            return True

    def delete_node(self, val):
        """
        Method to delete node with value val in the BST
        """
        self.delete_node_helper(self.head, val)

    def delete_node_helper(self, node, val):
        """
        Helper to delete the node with value val.
        """
        if node is None:
            return
        if node.val > val:
            node.left = self.delete_node_helper(node.left, val)
        elif node.val < val:
            node.right = self.delete_node_helper(node.right, val)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                temp = self.inorder_successor(node.right)
                node.val = temp.val
                node.right = self.delete_node_helper(node.right, temp.val)
        return node

    def inorder_successor(self, node):
        """
        Helper to return the inorder successor of a node
        """
        temp = node
        while temp.left is not None:
            temp = temp.left
        return temp

    def is_tree_bst(self):
        """
        Method to return True/False if the tree is a BST
        """
        return self.is_node_bst(self.head)

    def is_tree_balanced(self):
        """
        Method to return True/False is the tree is a balanced BST
        """
        if self.is_tree_bst() is False:
            return False
        temp = self.head
        return self.is_node_balanced(temp) and self.is_node_balanced(temp.left) and self.is_node_balanced(temp.right)

    def is_node_balanced(self, node):
        """
        Helper to tell us if the node is balanced
        """
        if Node is None:
            return True
        return abs(self.get_node_height(node.left) - self.get_node_height(node.right)) <= 1

    def get_node_height(self, node):
        """
        Helper to return the height of a node
        """
        if node is None:
            return -1
        return 1 + max(self.get_node_height(node.left), self.get_node_height(node.right))

    def is_node_bst(self, node):
        """
        Method to return True/False if the node is a BST or not
        """
        if node is None:
            return True
        if node.left is not None and node.left.val > node.val:
            return False
        if node.right is not None and node.right.val <= node.val:
            return False
        return self.is_node_bst(node.right) and self.is_node_bst(node.left)

    def show(self):
        """
        Method to display the full BST from the root
        """
        if self.head is None:
            print("Empty")
            return
        self.show_tree(self.head)

    def show_tree(self, node, right=True, indent=""):
        """
        Helper to show the tree starting from defined node
        """
        if node is not None:
            print(indent, end="")
            if right is True:
                if indent == "":
                    print("Head:", end="")
                else:
                    print("R--->", end="")
                if indent == "":
                    indent += "     "
                else:
                    indent += "|    "
            else:
                print("L--->", end="")
                indent += "     "
            print(node.val)
            self.show_tree(node.right, True, indent)
            self.show_tree(node.left, False, indent)


