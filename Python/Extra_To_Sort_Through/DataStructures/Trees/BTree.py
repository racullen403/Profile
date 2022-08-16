"""

A special self-balancing tree where a node can contain more than _01_BasicPython key and can have more than
two children, it's the generalised form of a BST.

These are useful in reducing the potential height of a tree since multiple nodes can be
"condensed"into a single node containing those keys. This can make access to the nodes much
faster.

B-Trees are used for secondary storage and so we use Disk-read and Disk-write operations, the
root of the tree is kept in main memory however (must disk-write if the root node is changed).

Properties:
    - Every node x contains the number of keys n(x), the n(x) keys themselves in increasing
    order, and a boolean to say whether it is a leaf or not.
    - If x is an internal node, it contains n(x)+_01_BasicPython pointers to its children.
    - The keys separate the ranges of keys stored in each subtree.
    - All leaves have the same depth (height of the tree).
    - There is a lower and upper bound on the number of keys a node contains, expressed by
    the minimum degree of the tree, t>=2:
        - All nodes other than root have at least t-_01_BasicPython keys, all internal nodes have at least t
        children, and the root has at least _01_BasicPython key(if tree is non empty).
        - All nodes have at most 2t-_01_BasicPython keys, an internal node has at most 2t children, a node is
        full if it has 2t-_01_BasicPython keys.

Height:
    - If n>=_01_BasicPython, then for any n-key B-Tree of height h and minimum degree t>=2

        h <= logt(n+_01_BasicPython)/2   (t base)

Searching:
    - Very similar to a BST except at each node we make an n(x)+_01_BasicPython decision for which tree to
    traverse down instead of just 2.
    - We return an index pointer i for the position in the node the key is at, and the key
    itself (key, i)

Insertion:
    - We insert at the root node, if it is non-full then we apply our non-full insertion method,
    if it is full we create an empty node and make it the new root while the old root becomes its child, we
    them split the child node and do our non-full insert on the new root.

Non-full insertion:
    - There are 2 cases, the node is a leaf or the node is an internal node.
    - If the node is a leaf, we simply find the position the new key belongs and insert it there.
    - If the node is an internal node, we find the insertion point as before, but then look into the left
    child of this key, if the left child is non-full then reapply the non-full insertion method on this
    child node, if it is full then apply the split method to child, this will raise the median, if the key
    being inserted is greater than the median then we non-full insert it into the next child along, else
    non-full insert it into the current child.

Split Child:
    - This method raises the median of a child node into the non-full node, and adds a new child node in
    corresponding positions.
    - If the child node being split isn't a leaf, then we must change the child pointers of the two
    split children

Deletion:
    - Search for node that contains key to delete, delete the key, re-balance the tree.
    - Look out for underflow, this is when the node contains less than the minimum number of keys (t-_01_BasicPython).
    - To re-balance we use the inorder successor and inorder predecessor where required.
    - There are 3 cases to consider when deleting:

        Case _01_BasicPython:
        - Key to delete lies in leaf.
        - If deleting it doesn't create underflow then we are done.
        - If deleting it does create underflow, we must borrow from the immediate sibling, check left has
        more than the minimum keys and then borrow (parent drops down to deleted key position, left sib
        key takes its place), else try the same with the right sib.
        - If we have underflow and the immediate siblings both have the minimum keys, merge the node with
        either the left or right sib (parent drops into node position and a sib merges to it)

        Case 2:
        - The key to be deleted lies in an internal node.
        - Delete key and replace with its inorder predecessor if the left child has more than t-_01_BasicPython keys.
        - If right child has more than t-_01_BasicPython keys then replace the key with its inorder successor.
        - If left and right have minimum keys, delete the key and merge its children.

        Case 3:
        - When the key to delete is an internal node and has minimum number of keys, tree height will
        shrink.
        - Look for a potential inorder predecessor or successor, if they don't exist (both minimum keys),
        then we merge the children and look for a sibling to borrow a key from, if they contain minimum keys
        then the node merges with the sibling along with the parent.

"""


class Node(object):

    def __init__(self, leaf=False):
        self.key = []
        self.leaf = leaf
        self.child = []


class BTree(object):

    def __init__(self, t):
        self.root = Node(True)      # We would write this to disk
        self.t = t                  # t is the minimum degree of the BTree, we specify this

    # method to search for key from specified node
    def search(self, node, key):
        i = 0
        while i < len(node.key) and key >= node.key[i]:
            i += 1
        if i < len(node.key) and key == node.key[i]:
            return node, i
        elif node.leaf is True:
            return None
        else:
            # you would disk-read(child_i) here to get the next page from the hard drive
            self.search(node.child[i], key)

    # method to insert an element into the BTree
    def tree_insert(self, key):
        root = self.root
        if len(root.key) == (2*self.t)-1:
            new_node = Node(False)
            self.root = new_node
            new_node.child.append(root)
            self.split_child(new_node, 0)
            self.insert_nonfull(new_node, key)
        else:
            self.insert_nonfull(root, key)

    # method to insert into a none full node
    def insert_nonfull(self, node, key):
        # find last index of keys
        i = len(node.key) - 1
        # if leaf
        if node.leaf is True:
            # add key to end
            node.key.append((key, i+1))
            # swap key down to its correct position
            while i >= 0 and key <= node.key[i]:
                node.key[i+1] = node.key[i]
                i -= 1
            node.key[i+1] = key
        # if not leaf
        else:
            # find index of child node it will go into
            while i >= 0 and key <= node.key[i]:
                i -= 1
            i += 1
            # if child is full, split it, moving the median into the current node
            if len(node.child[i].key) == (2*self.t)-1:
                self.split_child(node, i)
                # if key is bigger than median from split that got inserted, move index up _01_BasicPython
                if key > node.key[i]:
                    i += 1
            # apply nonfull insert to the correct child node
            self.insert_nonfull(node.child[i], key)

    # method to split a child node
    def split_child(self, node, i):
        t = self.t
        # pointer to child node we split
        child = node.child[i]
        # pointer to a new child node
        new = Node(leaf=child.leaf)
        # attach new node in i+_01_BasicPython position
        node.child.insert(i+1, new)
        # attach the median of the child into the i position of the node
        node.key.insert(i, child.key[t-1])
        # make the keys of the new child node those on the right of the median
        new.key = child.key[t: 2*t]
        # make the keys of the old child node those on the left of the median
        child.key = child.key[0: t-1]
        # if the child node we split was not a leaf
        if child.leaf is False:
            new.child = child.child[t: 2*t]
            child.child = child[0: t-1]

    # method to delete a key
    def b_delete(self, node, k):
        i = 0
        while i < len(node.key) and k > node.key[i]:
            i += 1
        if node.leaf is True:
            if i < len(node.key) and k == node.key[i]:
                node.key.pop(i)
                return
            return "Could not find node"

        # key is found at internal node
        if i < len(node.key) and k == node.key[i]:
            self.delete_internal_node(node, k, i)
        # key might be in child node that has more than minimum keys, we normal delete from it
        elif len(node.child[i].key) >= self.t:
            self.b_delete(node.child[i], k)
        # key might be in the child node that has a minimum number of keys
        else:
            



    # method to delete



    # method to show the tree in a meaningful way
    def show_tree(self, node, l=0):
        print("Level:", l, end=" Keys:")
        for i in node.key:
            print(i, end=" ")
        print()
        l += 1
        if len(node.child) > 0:
            for i in node.child:
                self.show_tree(i, l)


tree = BTree(2)
tree.tree_insert(50)
tree.tree_insert(25)
tree.tree_insert(75)
tree.tree_insert(10)
tree.tree_insert(5)
tree.tree_insert(8)
tree.show_tree(tree.root)
print("----Delete 25----")
tree.b_delete(25)
tree.show_tree(tree.root)
print("----Delete 5----")
tree.b_delete(5)
tree.show_tree(tree.root)
