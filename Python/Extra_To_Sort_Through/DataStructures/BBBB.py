class BNode:
    def __init__(self, leaf=False):
        self.key = []
        self.child = []
        self.leaf = leaf


class BTree:
    def __init__(self, t=2):
        self.t = t
        self.root = BNode(True)

    def b_insert(self, k):
        root = self.root
        if len(root.key) == (self.t * 2) - 1:
            new = BNode(False)
            self.root = new
            new.child.append(root)
            self.split_child(new, 0)
            self.non_full_insert(new, k)
        else:
            self.non_full_insert(root, k)

    def non_full_insert(self, node, k):
        i = len(node.key) - 1
        if node.leaf is True:
            node.key.append(k)
            while i >= 0 and k < node.key[i]:
                node.key[i+1] = node.key[i]
                i -= 1
            node.key[i+1] = k
        else:
            while i >= 0 and k < node.key[i]:
                i -= 1
            i += 1
            if len(node.child[i].key) < (self.t * 2) - 1:
                self.non_full_insert(node.child[i], k)
            else:
                self.split_child(node, i)
                if k < node.key[i]:
                    self.non_full_insert(node.child[i], k)
                else:
                    self.non_full_insert(node.child[i+1], k)

    def split_child(self, node, i):
        t = self.t
        old_child = node.child[i]
        new_child = BNode(old_child.leaf)
        median_node = old_child.key[t-1]
        node.key.insert(i, median_node)
        node.child.insert(i+1, new_child)
        new_child.key = old_child.key[t:]
        old_child.key = old_child.key[:t-1]
        if old_child.leaf is False:
            new_child.child = old_child.child[t:]
            old_child.child = old_child.child[:t]

    def show_tree(self, node, l=0):
        print("Level:", l, end=" Keys:")
        for i in node.key:
            print(i, end=" ")
        print()
        l += 1
        if len(node.child) > 0:
            for i in node.child:
                self.show_tree(i, l)

    def search(self, k):
        node = self.root
        i = 0
        while k != node.key[i] and i < len(node.key):
            if k < node.key[i]:
                node = node.child[i]
                i = 0
            else:
                i += 1
            if i == len(node.key):
                if node.leaf is True:
                    return "Could not find key"
                else:
                    node = node.child[i]
                    i = 0
        print(i, node.key)


tree = BTree()
tree.show_tree(tree.root)
a = [4, 10, 20, 5, 6, 5, 1, 2, 3, 0]
for i in a:
    print("--------------")
    tree.b_insert(i)
    tree.show_tree(tree.root, 0)


print("---Search 20---")
tree.search(20)