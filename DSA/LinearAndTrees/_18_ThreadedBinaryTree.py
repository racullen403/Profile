"""
Threaded Binary Tree:

    To explore a binary tree, we generally would apply a recursive algorithm, or add the nodes into a stack in some
    order depending on the traversal technique. This means we need an auxiliary data structure of size O(n) just to
    tell us the order to traverse the tree.

        e.g.    Inorder Traversal

                                          A
                                       /     \
                                      B       C
                                     / \     / \
                                    D   E   F   G

                Inorder: D B E A F C G

                We can achieve this in two ways,

                    Recursive Method:

                                lst_order = []
                                def inorder(root):
                                    if root:
                                        inorder(root.left)
                                        lst_order.append(root)
                                        inorder(root.right)


                    Stack Method:

                        - Use some stack S=[], initialise it to contain the root node S=[A] and set current=A.left,
                        now while current is not None, add is to S and repeat.

                        - If current is None and stack is not empty
                            - Pop top and add to list
                            - Set current to top.right
                            - repeat step of adding left terms to S until current is None

                        - If current is None and stack is empty, then we're done.


TBT Data Structure:

    Now, the major disadvantage of these methods is that traversal requires O(n) space complexity, we want a way to
    traverse the binary tree, with only O(1) extra space needed.

    One way we can do this is by extending our definition of the Binary Tree into a Threaded Binary Tree, in
    this case, we store extra information in the nodes so that at any given node, we can find the "next" node in the
    traversal order.

        - We say a binary tree is threaded if every right pointer that was previously None now points to the inorder
        successor, and all left pointers that were previously None now point to the inorder predecessor.

        e.g.    from before we got the inorder traversal D B E A F C G, so for nose D E F G that have None pointers,
                we would thread them.

                D.left = None
                D.right = B
                E.left = B
                E.right = A
                F.left = A
                F.right = C
                G.left = C
                G.right = None

        - Now we can do an inorder traversal as follows:

            current = inorder predecessor of root, ie the left most node

            while currents right pointer is threaded, move along, current = current.right

            if we reach a None threaded node, we move current to its inorder predecessor and repeat

            do this until current is None.


        - Note that single threaded means only left OR right pointer is threaded, double is when we thread both.


    Method 1:
        We thread a Binary Tree by simply doing an Inorder Traversal and storing the nodes in a queue. Now that we
        have the order we want, we thread the nodes together in our new data structure. The new node representations
        will need 1 extra field to say whether the pointer is threaded or not.

            class Node:

                def __init__(self, val):
                    self.val = val
                    self.left = None
                    self.right = None
                    self.rightThread = False
                    self.leftThread = False

    Method 2:
        A more space efficient way, instead of using a queue, is to use the fact that we link from the
        inorder predecessor which lie in the subtree of a node, to the node itself.


                                          A
                                       /     \
                                      B       C
                                     / \     / \
                                    D   E   F   G

                Inorder: D B E A F C G

                e.g.    Take E, it is the inorder predecessor of A and is threaded to A.
                        D is the inorder predecessor of B and gets threaded to B, same with F and C.

        We can use this idea to thread the nodes recursively instead of forming an O(n) queue, it will be O(logn) now.

            - If node has a left node, then we find the nodes inorder predecessor and link it to node.

        This method now means we can traverse the threaded tree in O(n) time like before, but with O(1) space, simply
        by adding another field to the tree and threading leaf nodes.


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

    def inorder_recursion(self):
        lst = []

        def add(node):
            if node:
                add(node.left)
                lst.append(node.val)
                add(node.right)

        root = self.root
        add(root)
        print("\nInorder using recursion:", lst)

    def inorder_stack(self):
        lst = []
        s = []
        current = self.root
        if not current:
            return
        s.append(current)
        current = current.left
        while s:
            while current:  # Add all left terms to stack
                s.append(current)
                current = current.left
            top = s.pop()
            lst.append(top.val)
            if top.right:
                s.append(top.right)
                current = top.right.left
        print("\nInorder using stack:", lst)
        return s


class ThreadedNode:

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.right_threaded = False


class ThreadedBinaryTree:

    def __init__(self, root):
        self.root = self.create_threaded_tree(root)

    def create_threaded_tree(self, root, thread=None):
        """
        root is standard Tree class object

        This used method 2 above, threading the nodes as we create the tree recursively
        """
        if root is None:
            return None
        new_node = ThreadedNode(root.val)
        if root.left:
            new_node.left = self.create_threaded_tree(root.left, new_node)
        if root.right:
            new_node.right = self.create_threaded_tree(root.right, thread)
        if not root.right:
            new_node.right = thread
            new_node.right_threaded = True
        return new_node

    def traversal(self):
        inorder = []
        current = self.root
        while current.left:
            current = current.left
        while current:
            inorder.append(current.val)
            if current.right_threaded:
                current = current.right
            else:
                current = current.right
                while current.left:
                    current = current.left
        return inorder


# example of binary tree traversal using recursion and using a stack
def example():
    t = Tree()
    t.create_tree()
    t.show_tree()
    t.inorder_recursion()
    t.inorder_stack()


# example of binary tree converted to threaded tree, we can see how the tree now loops back on itself
def example2():
    t = Tree()
    t.create_tree()
    t.show_tree()
    threaded = ThreadedBinaryTree(t.root)
    print("Traversal of the threaded nodes:", threaded.traversal())



