"""
A-B Tree

    An a-b tree is a self-balancing search tree that contains all leaf nodes at the same level. It can be defined as
    follows:
        - Each internal node (except root) has at least "a" children and at most "b" children.
        - The root has at most b children.
        - We require a and b to be positive integers such that 2 <= a <= (b+1)/2

        It follows logically that if a node has a minimum of "a" children and a maximum of "b"  children, then there
        is a minimum of a-1 keys and a maximum of b-1 keys, i.e. if order of a node (number of children) is t, then
        there are t-1 keys in the node.

    Representation:
        - We represent the tree using lists. Each node will have a list containing its keys, and a list containing the
        children nodes. The node at index i in the child list, will be the left child of the key at index i and the
        right child of the key will be at i+1.
        - We could also keep store the number of keys/child nodes for easier checking of overflow and underflow,
        however, lists in python take care of this.

    INSERTION:
        - We insert a key into its correct place in the leaf node.
        - Check for overflow, i.e. more than b-1 keys.
        - If we have overflow, split the node about the middle key:
            - Middle key moves up into the parent node keys (at same index the current child node it comes from is at).
            - Keys left of the middle one form the keys of a new left node, with child nodes up to and including the
            index of the middle key becoming the left nodes children. The remaining keys and nodes form a new right
            node. These new left and right nodes replace the original node in the child nodes of the parent.
            - Finally check the parent keys for overflow. This process repeats up the tree to the root.

    DELETION:
        We always delete from the leaf node, if key is found in an internal node, we replace it with its inorder
        successor and continue to try and delete the inorder successor key. Once key has been deleted, we must
        check for underflow:
            - Underflow when number of keys is less than a-1 (the minimum allowed)

                Case 1:
                    - Left sibling node has more than a-1 keys, so we borrow the right most key

                                [2,     4,     7]
                             /      |      |       \
                       [0, 1]     []   [5, 6]      [8, 9]

                       Suppose the node [] is the one with underflow as we have just removed its key.
                       We borrow 1 from its left sib by "rotating" into the underflow node

                                [1,     4,     7]
                             /      |      |       \
                          [0]      [2]   [5, 6]      [8, 9]

                Case 2:
                    - The left sibling has a-1 keys but the right sibling has more than a-1, so we can borrow from
                    the right sibling. Take the above example but rotate the right sibling's left mose key this time.


                                [2,     5,     7]
                             /      |      |       \
                       [0, 1]     [4]    [6]      [8, 9]

                Case3:
                    - Neither the left nor right sibling have enough keys to allow us to borrow one. In this case, we
                    must fuse the children.

                                [2,     4,     7]
                             /      |      |       \
                          [1]     []     [5]      [8, 9]

                    - If left sibling exists, i.e. underflow node isn't index 0, we combine left sib [1] and its
                    parent 2 into a node [1, 2] and place it into the child position replacing [1] and []

                                       [4,     7]
                                     |      |       \
                                 [1, 2]     [5]      [8, 9]

                    - In the case where index of child was 0, we would combine the parent and right child into a node
                    and do the same as before i.e.

                                [1,     4,     7]
                             /      |      |       \
                          []      [2]     [5]      [8, 9]


                                  [4,     7]
                                |      |       \
                           [1, 2]     [5]      [8, 9]

                    - We now must move up the tree and check the parent node for underflow since a key was removed
                    from it.

"""


class Node:

    def __init__(self):
        self.keys = None
        self.children = None
        self.parent = None


class ABT:
    def __init__(self, a, b):
        self.root = None
        self.a = a
        self.b = b

    def insert_key(self, key):
        if not self.root:
            self.root = Node()
            self.root.keys = [key]
        else:
            x = self.root
            found = False
            while not found:  # Look for leaf node to insert into, x will point to it at end of loop
                if not x.children:
                    found = True
                else:
                    i = 0
                    while i < len(x.keys) and x.keys[i] < key:
                        i += 1
                    x = x.children[i]
            x.keys.append(key)
            i = len(x.keys) - 1
            while i > 0:  # Place key into keys list, and swap it into place
                if x.keys[i] >= x.keys[i - 1]:
                    break
                x.keys[i], x.keys[i - 1] = x.keys[i - 1], x.keys[i]
                i -= 1
            while len(x.keys) == self.b:  # Overflow, split and fix the tree
                mid = self.b // 2
                left_node = Node()
                left_node.keys = x.keys[:mid]
                right_node = Node()
                right_node.keys = x.keys[mid + 1:]
                if x.children:
                    left_node.children = x.children[:mid + 1]
                    for child in left_node.children:
                        child.parent = left_node
                    right_node.children = x.children[mid + 1:]
                    for child in right_node.children:
                        child.parent = right_node
                if not x.parent:  # Case when we push middle key into new root position
                    root = Node()
                    root.keys = [x.keys[mid]]
                    root.children = [left_node, right_node]
                    left_node.parent = root
                    right_node.parent = root
                    self.root = root
                    x = self.root
                else:  # Case when middle key is pushed into an internal node
                    p = x.parent
                    left_node.parent = p
                    right_node.parent = p
                    p.keys.append(x.keys[mid])
                    i = len(p.keys) - 1
                    while i > 0:
                        if p.keys[i] >= p.keys[i - 1]:
                            break
                        p.keys[i], p.keys[i - 1] = p.keys[i - 1], p.keys[i]
                        i -= 1
                    p.children = p.children[:i] + [left_node, right_node] + p.children[i + 1:]
                    x = p

    def delete_key(self, key):
        if not self.root:  # No tree
            return
        x = self.root
        deleted = False
        while not deleted:
            i = 0
            while i < len(x.keys) and x.keys[i] < key:
                i += 1
            if not x.children and (i == len(x.keys) or x.keys[i] != key):  # Key not found
                return
            elif i == len(x.keys) or x.keys[i] != key:  # Check ith child for key
                x = x.children[i]
            else:  # Found key
                if x.children:  # Internal node, find successor
                    inorder = self.inorder_successor(x.children[i + 1])
                    x.keys[i] = inorder.keys[0]
                    key = inorder.keys[0]
                    x = inorder
                else:  # Leaf node, this is where we remove key
                    x.keys = x.keys[:i] + x.keys[i + 1:]
                    deleted = True
        while len(x.keys) < self.a - 1:  # Underflow condition
            if x == self.root:
                if len(x.keys) == 0:
                    self.root = None
                return
            i = 0
            while x.parent.children[i] != x:  # Find which child x is
                i += 1
            if i > 0 and len(x.parent.children[i-1].keys) >= self.a:  # Case 1: We can take key from left sib
                p = x.parent.keys[i - 1]
                left_sib_key = x.parent.children[i - 1].keys.pop()
                x.parent.keys[i - 1] = left_sib_key
                x.keys = [p] + x.keys
            elif len(x.parent.children[i + 1].keys) >= self.a:  # Case 2: We take from right sib
                p = x.parent.keys[i]
                right_sib_key = x.parent.children[i + 1].keys[0]
                x.parent.children[i + 1].keys = x.parent.children[i + 1].keys[1:]
                x.keys.append(p)
                x.parent.keys[i] = right_sib_key
            else:  # Case 3: fuse nodes
                if i == 0:
                    p = x.parent.keys[0]
                    x.parent.keys = x.parent.keys[1:]
                    x.parent.children = x.parent.children[1:]
                    x.parent.children[0].keys = x.keys + [p] + x.parent.children[0].keys
                    if x.children:
                        for child in x.children:
                            child.parent = x.parent.children[0]
                        x.parent.children[0].children = x.children + x.parent.children[0].children
                else:
                    p = x.parent.keys[i-1]
                    x.parent.keys = x.parent.keys[:i-1] + x.parent.keys[i+1:]
                    x.parent.children = x.parent.children[:i] + x.parent.children[i+1:]
                    x.parent.children[i-1].keys += [p] + x.keys
                    if x.children:
                        for child in x.children:
                            child.parent = x.parent.children[i-1]
                        x.parent.children[i-1].children += x.children
            x = x.parent

    def inorder_successor(self, node):
        while node.children:
            node = node.children[0]
        return node

    def show(self):
        def show_r(node, count):
            if node:
                if count == -1:
                    print("ROOT", end=" ")
                count += 1
                print(node.keys)
                if node.children:
                    for i in range(len(node.children)):
                        print("    " + "    |   " * count, end="")
                        print("child", i + 1, "->", end=" ")
                        show_r(node.children[i], count)
        show_r(self.root, -1)


# Example of insertion
def example1():
    abt = ABT(2, 3)
    for i in range(20):
        print("\n----- Insert {} -----".format(i))
        abt.insert_key(i)
        abt.show()


# Example of deletion
def example2():
    abt = ABT(2, 3)
    for i in range(10):
        abt.insert_key(i)
    print("\n----- Initial Tree -----")
    abt.show()
    d = 7
    abt.delete_key(d)
    print("\n----- Final Tree -----")
    abt.show()


example2()



