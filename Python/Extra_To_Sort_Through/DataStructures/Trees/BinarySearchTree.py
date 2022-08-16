"""
A Binary Search Tree is a sorted tree data structure whose nodes have a maximum of 2 children.

Its defining properties:
    - All nodes in the left subtree are smaller than the root node
    - All nodes in the right subtree are greater than the root node
    - All subtrees also display these properties

With data sorted in this way we can search for a specific node in O(logn) time, and insert/delete
in the same.
"""


class Node(object):

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def preorder_show(self):
        print(self.value, end=" ")
        if self.left:
            self.left.preorder_show()
        if self.right:
            self.right.preorder_show()


# function to insert into a binary search tree
def bst_insert(node, value):
    if value < node.value and node.left:
        return bst_insert(node.left, value)
    elif value > node.value and node.right:
        return bst_insert(node.right, value)
    elif value < node.value and node.left is None:
        node.left = Node(value)
    else:
        node.right = Node(value)


# function to create a bst from an array
def bst(arr):
    root = Node(arr[0])
    for i in range(1, len(arr)):
        bst_insert(root, arr[i])
    return root


# function to search for element in bst and return corresponding node if exists
def bst_search(node, value):
    if node.value == value:
        return node
    elif node.left and value < node.value:
        return bst_search(node.left, value)
    elif node.right and value > node.value:
        return bst_search(node.right, value)
    else:
        return


# function to delete from the bst
def bst_delete(node, value):
    if node is None:
        return node
    if value < node.value:
        node.left = bst_delete(node.left, value)
    elif value > node.value:
        node.right = bst_delete(node.right, value)
    else:
        if node.left is None:
            temp = node.right
            node.right = None
            return temp
        elif node.right is None:
            temp = node.left
            node.left = None
            return temp
        else:
            temp = node.right
            successor = inorder_successor(temp)
            node.value = successor.value
            successor.value = value
            return bst_delete(temp, value)


def inorder_successor(node):
    if node.left is None and node.right is None:
        return node
    elif node.left:
        return inorder_successor(node.left)
    else:
        return inorder_successor(node.right)


""" 
Example:
    Let's create the following tree
    
            5
        3       8
      _01_BasicPython   4   6   9
"""

print("\n----Preorder of out BST----")
arr = [5, 3, 8, 1, 4, 6, 9]
tree = bst(arr)
tree.preorder_show()
print("\n----End----")
print("\n----Search for each of the elements")
for i in arr:
    if bst_search(tree, i).value == i:
        print("Found:", bst_search(tree, i).value)
    else:
        print("Couldn't find:", i)
print("Search for 10:", bst_search(tree, 10))
print("----End----")

""" 
Example:
    Let's delete 5 from previous tree

            6
        3       8
      _01_BasicPython   4      9
"""


print("\n----Delete 5----")
bst_delete(tree, 5)
print("Search for 5:", bst_search(tree, 5))
print("New root after deletion:", tree.value)
print("Check where 6 used to be:", tree.right.left)
print("----End----")