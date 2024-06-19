class Tree:

    def __init__(self, id, priority):
        self.val = priority  # Value of the node
        self.id = id  # id mapping to further information
        self.children = []  # Root list of child trees
        self.parent = None  # Pointer to parent node
        self.mark = False  # Indicate if the node has had a child cut

    def rank(self):
        return len(self.children)


class FibHeap:

    def __init__(self):
        self.heap = []  # Root list, min stored at last position
        self.lookup = {}  # Lookup of nodes in the heap, allows O(1) searching for decrease key

    def insert(self, id, priority):
        """
        - Add new tree t=Tree(key) to the heap.
        - If the new key is larger than the previous root key, swap them, this
        ensures the minimum key is always at the last tree in the list.
        - Fast O(1) insert
        """
        if id in self.lookup:
            return
        t = Tree(id, priority)
        self.lookup[id] = t
        self.heap.append(t)
        if len(self.heap) > 1 and self.heap[-1].val > self.heap[-2].val:
            self.heap[-1], self.heap[-2] = self.heap[-2], self.heap[-1]

    def del_min(self):
        if self.heap:
            m = self.heap.pop()
            del self.lookup[m.id]
            for child in m.children:
                child.parent = None
                child.mark = False
                self.heap.append(child)
            self.consolidate()
            return m.id
        return

    def consolidate(self):
        if self.heap:
            ranks = {}
            for i in range(len(self.heap)):
                temp = self.heap[i]
                while temp.rank() in ranks and ranks[temp.rank()] is not None:
                    ttemp = ranks[temp.rank()]
                    ranks[temp.rank()] = None
                    if ttemp.val < temp.val:
                        ttemp, temp = temp, ttemp
                    temp.children = [ttemp] + temp.children
                    ttemp.parent = temp
                ranks[temp.rank()] = temp
            new_heap = []
            i = 0
            for k, v in ranks.items():
                if ranks[k] is not None:
                    new_heap.append(v)
                    if v.val < new_heap[i].val:
                        i = len(new_heap) - 1
            new_heap[i], new_heap[-1] = new_heap[-1], new_heap[i]  # place min at the end of the root list
            self.heap = new_heap

    def decrease_key(self, id, priority):
        if id in self.lookup and priority < self.lookup[id].val:
            temp = self.lookup[id]
            temp.val = priority
            if temp.parent and temp.val < temp.parent.val:
                self.cascade_cut(id)

    def cascade_cut(self, id):
        temp = self.lookup[id]
        i = 0
        for child in temp.parent.children:
            if child == temp:
                break
            i += 1
        temp.parent.children.pop(i)
        parent = temp.parent
        temp.parent = None
        temp.mark = False
        self.heap.append(temp)
        if self.heap[-1].val > self.heap[-2].val:
            self.heap[-1], self.heap[-2] = self.heap[-2], self.heap[-1]
        if parent.parent:
            if parent.mark is False:
                parent.mark = True
            else:
                self.cascade_cut(parent.id)

    def show(self):
        spacer = "    "
        indent = "|          "

        def dfs_show(explore, count=0):
            """
            DFS to explore each node:
                - Node is popped, its child nodes are printed and then
                added to the explore stack
            """
            if explore:  # Explore the child nodes
                node = explore.pop()
                print(spacer + indent * count, end="")
                for i in range(len(node.children)):
                    if i != 0:
                        print("---", end="")
                    m = "T"
                    if not node.children[i].mark:
                        m = "F"
                    print((node.children[i].val, m), end="")
                    if i < len(node.children) - 1:
                        explore.append(node.children[i])
                        count += 1
                print()
                print(spacer + indent * count)
                count -= 1
                dfs_show(explore, count)

        print("--------")
        print("Fibonacci Heap")
        print("--------")

        for i in range(len(self.heap)):
            if i < len(self.heap) - 1:
                print("\n Tree rooted at index:", i)
            else:
                print("\n Tree (MIN) rooted at index:", i)
            print("    " + str(self.heap[i].val))
            print("    |")
            dfs_show([self.heap[i]])


# Example of lazy insert in O(1) time
def example():
    print("Inserting 1-10 nodes:")
    h = FibHeap()
    for i in range(1, 11):
        h.insert(i, i)
    h.show()
    print("\nDELETE MIN", h.del_min())
    h.show()
    print("\nDELETE MIN", h.del_min())
    h.show()
    print("\nDELETE MIN", h.del_min())
    h.show()


def example2():
    h = FibHeap()
    for i in range(11):
        h.insert(i, i)
    print("\nInsert 0-10 into heap:")
    h.show()
    print("\nExtract Min: ", end="")
    print(h.del_min())
    h.show()
    print("Decrease 7 -> 4: ")
    h.decrease_key(7, 4)
    h.show()
    print("Is 5 marked:", h.lookup[5].mark)
    print("Lets cut 6, 6 -> 3:")
    h.decrease_key(6, 3)
    h.show()


example2()