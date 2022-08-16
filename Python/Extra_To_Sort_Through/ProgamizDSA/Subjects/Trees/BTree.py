"""
B-Tree:
    This is a self-balancing search tree.
    Used when we are storing more data than can be used in main memory.
    When we have a high number of keys, data is read off the disk in blocks, these access times are very high compared
        to main memory, as a result, we want to reduce the number of disk accesses. We achieve this by storing as much
        data as we can at each Node (usually equal to disk block size).
    The result of this is a shorter and fatter tree, this significantly reduces read times compared to an AVL or
        Red-Black Tree.

Properties:
    All leaves are at the same level
    Defined by minimum degree t (usually depends on disk block size), all nodes except root contain at least t-1 keys
        (root can have 1). All nodes have at most 2t-1 keys, including root.
    If node has k keys, it has k+1 children, except leaf nodes.
    Keys are sorted in increasing order, child node between k1 and k2 contains all keys in the range k1<k<k2.
    B-Tree grows and shrinks from the root unlike BST which grow and shrink downwards.
    Time complexity of search/insert/delete is O(logn)
    Insertion of a key only occurs at a Leaf Node.

Search:
    We start from root and recursively search down the tree for some key k. If k is not in the node, we search the
        appropriate child node, if we find k, return the Node (and index). If we don't find k and are in a Leaf Node,
        we return NULL.

Insert:
    We always insert at the leaf node.
    Starting from the root, we traverse down until we reach the leaf node where key k is to be inserted. We already
        know how many keys a node can contain, so before inserting, we make sure the node has space, we do this by
        pre-emptively splitting the node if it is full.
    Starting from root x, while x is not a leaf we do the following:
        - Find the child node y that key k will be inserted into.
        - If y is not full, change x from root to y
        - If y is full, we split y and make x point to the child node k would lie in.
        Once we find a leaf node, we know k can be inserted here due to the pre-emptive splits.
    We call this a proactive insertion method, splitting nodes before actually traversing them, this ensures we do not
        travers nodes twice. The main disadvantages of this is we may do unnecessary splits, however, it prevents
        cascading splits up the tree.

Child Split:
    If we have some node x and have determined key k will be (attempted to be) inserted into its child y, we must check
        if y is full or not. If y is full then it must first be split to ensure k can be inserted. Note, k may not
        actually be inserted into y as it may not be a leaf node, however, this pre-emptive split ensures that if
        further splits down the tree occur, the key that gets propagated upwards (this is why Btrees grow upwards) will
        never run into a full node. When y is split, we propagate the median key into the parent node keys, and form 2
        child nodes from the remaining keys y and z.

Delete:
    Deletion can occur at both the leaf node and the internal node.
    - Deleting from an internal node will result in the children being rearranged.
    - We also need to take into account the minimum degree of the tree (root can have 1 key, nodes t-1 minimum)
    Just like with the insert method, we want to only pass down the tree once, this means we require each node
        visited to have at least t keys in it, that way if deletion occurs at the node, we will still have the
        minimum keys required.
    Procedure:
        - If node x is a leaf and key k is in it, delete k
        - If node x is an internal node and contains key k:
            -> If preceding child y of key k has at least t keys, let the inorder predecessor be k0 from y, replace k
            in x with k0 and recursively apply deletion of key k0 in child node y.
            -> If y has less than t keys, we look to the right child z, if z has at least t keys, let the inorder
            successor be k0 from z, replace k with k0 in x and recursively apply deletion of key k0 to child node z.
            -> If both y and z child nodes have fewer than t keys, merge key k and z into y (x loses k and z) and
            recursively apply deletion of key k in child node y.
        - If key k is not in internal node x, determine appropriate child y key k would lie in. If y has more than t-1
        keys, recursively apply deletion of key k on node y. If y has fewer than t children:
            -> If y has an immediate sibling with at least t keys, move the key from x down into child y and move
            appropriate inorder successor/predecessor up into x
            -> If y and both it's immediate siblings have t-1 keys, merge y with an appropriate sibling and the key
            from x as a median key for this node. Recursively apply deletion of key k from this child node y.

"""


class BNode:

    def __init__(self, leaf=False):
        self.keys = []
        self.children = []
        self.leaf = leaf


class BTree:

    def __init__(self, t):
        self.root = BNode(True)
        self.t = t

    def search(self, node, key):
        i = 0
        while i < len(node.keys):
            if node.keys[i] == key:
                return node, i
            elif key > node.keys[i]:
                i += 1
            else:
                break
        if i < len(node.children):
            self.search(node.children[i], key)
        return

    def insert(self, key):
        root = self.root
        if len(root.keys) == 2*self.t - 1:
            temp = BNode(False)
            temp.children.append(root)
            self.root = temp
            self.split_child(temp, 0)
            self.non_full_insert(temp, key)
        else:
            self.non_full_insert(root, key)

    def non_full_insert(self, node, key):
        i = len(node.keys) - 1
        if node.leaf is True:
            node.keys.append(key)
            while i >= 0 and key < node.keys[i]:
                node.keys[i+1] = node.keys[i]
                i -= 1
            node.keys[i+1] = key
        else:
            while i >= 0 and key < node.keys[i]:
                i -= 1
            i += 1
            if len(node.children[i].keys) == 2*self.t - 1:
                self.split_child(node, i)
                if key > node.keys[i]:
                    i += 1
            self.non_full_insert(node.children[i], key)

    def split_child(self, node, i):
        mid = self.t - 1
        y = node.children[i]
        z = BNode(y.leaf)
        node.keys.insert(i, y.keys[mid])
        node.children.insert(i+1, z)
        z.keys = y.keys[mid+1:]
        y.keys = y.keys[:mid]
        if y.leaf is False:
            z.children = y.children[mid+1:]
            y.children = y.children[:mid+1]

    def delete_key(self, node, key):
        t = self.t
        i = 0
        while i < len(node.keys) and key > node.keys[i]:
            i += 1
        if node.leaf is True:
            if i < len(node.keys):
                node.keys.pop(i)
            else:
                print("No key found")
                return
        elif i < len(node.keys) and node.keys[i] == key:
            y = node.children[i]
            z = node.children[i + 1]
            if len(y.keys) >= t:
                temp = self.inorder_predeccessor(y)
                node.keys[i] = temp.keys[-1]
                self.delete_key(y, temp.keys[-1])
            elif len(z.keys) >= t:
                temp = self.inorder_successor(z)
                node.keys[i] = temp.keys[0]
                self.delete_key(z, temp.keys[0])
            else:
                self.child_merge(node, i)
                self.delete_key(node.children[i], key)
        else:
            y = node.children[i]
            if len(y.keys) >= t:
                self.delete_key(y, key)
            else:
                if i > 0 and len(node.children[i-1].keys) >= t:
                    y.keys.insert(0, node.keys[i-1])
                    node.keys[i-1] = node.children[i-1].keys[-1]
                    y.children.insert(0, node.children[i-1].children[-1])
                    node.children[i-1].keys.pop()
                    node.children[i-1].children.pop()
                    self.delete_key(y, key)
                elif i < len(node.keys) and len(node.children[i+1].keys) >= t:
                    y.keys.append(node.keys[i])
                    node.keys[i] = node.children[i+1].keys[0]
                    y.children.append(node.children[i+1].children[0])
                    node.children[i+1].keys.pop(0)
                    node.children[i+1].children.pop(0)
                    self.delete_key(y, key)
                else:
                    self.child_merge(node, i)
                    self.delete_key(node.children[i], key)

    def child_merge(self, node, i):
        if i == len(node.keys):
            i -= 1
        k = node.keys[i]
        y = node.children[i]
        z = node.children[i+1]
        y.keys.append(k)
        y.keys += z.keys
        if y.leaf is False:
            y.children += z.children
        node.keys.pop(i)
        node.children.pop(i+1)

    def inorder_successor(self, node):
        temp = node
        while temp.leaf is False:
            temp = temp.children[0]
        return temp

    def inorder_predeccessor(self, node):
        temp = node
        while temp.leaf is False:
            temp = temp.children[-1]
        return temp

    def show(self, node, l=0):
        print("Level", l, " : ", end="")
        for i in node.keys:
            print(i, end=" ")
        print()
        l += 1
        if node.leaf is False:
            for child in node.children:
                self.show(child, l)


t1 = BTree(2)
for i in list(range(10)):
    print("-------------")
    print("Insert:", i)
    t1.insert(i)
    t1.show(t1.root)

t1.delete_key(t1.root, 0)
print("----------")
t1.show(t1.root)


