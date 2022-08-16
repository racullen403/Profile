"""
In Our BST class we implemented ways in which to check if the tree is balanced and methods to find the heights of
nodes. We will now create an AVL Tree which contains methods to rotate nodes in the BST so that the tree remains
in a balanced state, this is very useful as it reduces worst case conditions.

We ensure that every Node() is balanced, ie the difference in heights of left and right sub-trees is always <=1. We
call this the balance factor of the node/tree, it should always be -1, 0, or 1.
"""


class Node:
    """
    Basic Node class without height attribute, we will have to calc heights using a method in the AVL class
    """
    def __init__(self, val=None):
        self.val = val
        self.left = None
        self.right = None


class AVL:

    def __init__(self, head=None):
        self.head = head

    def insert(self, val):
        """
        Method to insert a value into the AVL tree and maintain its balance
        """
        self.head = self.insert_node(self.head, val)

    def insert_node(self, node, val):
        """
        Helper to insert value using BST method
        """
        if node is None:
            return Node(val)
        else:
            if val < node.val:
                node.left = self.insert_node(node.left, val)
            else:
                node.right = self.insert_node(node.right, val)
        balance = self.get_balance(node)
        if balance > 1:
            if val < node.left.val:
                return self.right_rotate(node, node.left)
            else:
                node.left = self.left_rotate(node.left, node.left.right)
                return self.right_rotate(node, node.left)
        if balance < -1:
            if val > node.right.val:
                return self.left_rotate(node, node.right)
            else:
                node.right = self.right_rotate(node.right, node.right.left)
                return self.left_rotate(node, node.right)
        return node

    def delete(self, val):
        """
        Method to delete a value from the AVL tree and maintain its balance
        """
        self.head = self.delete_node(self.head, val)

    def delete_node(self, node, val):
        """
        Method to delete the node with value val and maintain the balance of the tree
        """
        if node is None:
            return
        if val < node.val:
            node.left = self.delete_node(node.left, val)
        elif val > node.val:
            node.right = self.delete_node(node.right, val)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            else:
                temp = self.inorder_successor(node.right)
                node.val = temp.val
                node.right = self.delete_node(node.right, temp.val)
        balance = self.get_balance(node)
        if balance > 1:
            if self.get_balance(node.left) >= 0:
                return self.right_rotate(node, node.left)
            else:
                node.left = self.left_rotate(node.left, node.left.right)
                return self.right_rotate(node, node.left)
        if balance < -1:
            if self.get_balance(node.right) <= 0:
                return self.left_rotate(node, node.right)
            else:
                node.right = self.right_rotate(node.right, node.right.left)
                return self.left_rotate(node, node.right)
        return node

    def inorder_successor(self, node):
        """
        Method for finding the inorder successor of a node
        """
        temp = node
        while temp.left:
            temp = temp.left
        return temp

    def get_balance(self, node):
        """ 
        Helper to get the balance factor of a given node
        """
        return self.get_height(node.left) - self.get_height(node.right)
        
    def get_height(self, node):
        """ 
        Helper to get the height of a given node
        """
        if node is None:
            return -1 
        else:
            return 1 + max(self.get_height(node.left), self.get_height(node.right))

    def left_rotate(self, node1, node2):
        """
        Helper to perform a left rotation on node1 and its right child node2, returning node2 to be attached to the 
        parent of node1. A
        """
        node1.right = node2.left
        node2.left = node1
        return node2
    
    def right_rotate(self, node1, node2):
        """ 
        Helper to perform a right rotation on node1 and its left child node2, returning node2 to be attached to the 
        parent of node1
        """
        node1.left = node2.right 
        node2.right = node1 
        return node2

    def is_balanced(self):
        """
        Method to check if the whole tree is balanced
        """
        return self.is_tree_balanced(self.head)

    def is_tree_balanced(self, node):
        """
        Method to check if a node is balanced and its sub-nodes are also balanced
        """
        if node is None:
            return True
        if self.get_balance(node) not in [0, 1, -1]:
            return False
        else:
            return self.is_tree_balanced(node.left) and self.is_tree_balanced(node.right)

    def show(self):
        """
        Method to help show a useful representation of the tree
        """
        self.show_tree(self.head, "", True)

    def show_tree(self, node, indent, right):
        """
        Helper to show a useful representation of the tree
        """
        if node is not None:
            print(indent, end="")
            if right is True:
                if indent == "":
                    print("Head:", end="")
                else:
                    print("R--->", end="")
                if indent == "":
                    indent = "     "
                else:
                    indent += "|    "
            else:
                print("L--->", end="")
                indent += "     "
            print(node.val)
            self.show_tree(node.right, indent, True)
            self.show_tree(node.left, indent, False)

    def show_tree_detail(self, node, indent, right):
        """
        Helper to show a useful representation of the tree
        """
        if node is not None:
            print(indent, end="")
            if right is True:
                if indent == "":
                    print("Head:", end="")
                else:
                    print("R--->", end="")
                if indent == "":
                    indent = "     "
                else:
                    indent += "|    "
            else:
                print("L--->", end="")
                indent += "     "
            print(node.val, "({})".format(self.get_balance(node)))
            self.show_tree_detail(node.right, indent, True)
            self.show_tree_detail(node.left, indent, False)
