"""
Morris Traversal:

    This is a technique similar to the threaded binary tree idea, except we can do everything inplace in the normal
    tree structure, and revert the changes back, giving us the inorder traversal of a tree without using an additional
    space requirements (ie auxiliary arrays or extra fields in objects)

    Take
                     A
                   /  \
                  B    C
                 /\    /\
                D  E  F  G

    With the threaded tree, we would want to thread D->B, E->A, F->C, we can achieve this as follows.

        Let current=root,
            - if current.left is None, we are at the inorder predecessor and add it to the list, move current to
            current.right.
            - if current.left is not None, then we know something must be threaded to current, so we find the inorder
            successor in the left subtree of current (the rightmost child) and link it to current. Note that this will
            be the node whose right child is None, or already points to current as it is threaded already.
                - if this node.right is current, set it to None, add value to list, go to current.right
                - if node.right is None, link it to current, go to current.left

        Essentially, we are threading nodes to their inorder successors until we reach the left most node, at which
        point we print it and then move to the node it was threaded to, in doing so we have started a loop, now we will
        try to thread a node that was already threaded, this indicates to us that everything in the left subtree is
        explored, so we print current node, traverse the left subtree to remove the thread to None, and move into the
        right subtree.


"""


class Node:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Tree:

    def __init__(self):
        self.root = None

    def add_node(self, val):
        temp = self.root
        if not temp:
            self.root = Node(val)
            return
        node = self.root
        parent = None
        while node:
            parent = node
            if val <= node.val:
                node = node.left
            else:
                node = node.right
        if val <= parent.val:
            parent.left = Node(val)
        else:
            parent.right = Node(val)

    def create_tree(self):
        nodes = [4, 2, 6, 1, 3, 5, 7]
        for node in nodes:
            self.add_node(node)

    def show_tree(self):
        root = self.root
        spacer = "     "
        gap = "|    "

        def show(node, left, count):
            if node:
                if node is not self.root:
                    print(spacer + gap * count, end="")
                    if left:
                        print("|--> L:", end="")
                    else:
                        print("|--> R:", end="")
                else:
                    print("Root:", end="")
                print(node.val)
                show(node.left, True, count + 1)
                show(node.right, False, count + 1)

        show(root, True, -1)


def morris_traversal(root):
    inorder = []
    current = root
    while current:
        if current.left:
            temp = current.left
            while temp.right and temp.right != current:
                temp = temp.right
            if temp.right is None:
                temp.right = current
                current = current.left
            else:
                temp.right = None
                inorder.append(current.val)
                current = current.right
        else:
            inorder.append(current.val)
            current = current.right
    return inorder


def example():
    t = Tree()
    t.create_tree()
    t.show_tree()
    order = morris_traversal(t.root)
    print(order)


example()
