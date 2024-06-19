"""
Disjoint Set Union:

    This is a data structure used for storing disjoint sets (non overlapping sets). It has two main operations,
    joining of two disjoint sets into one, and finding which set an element belongs to. We must initially be able to
    create a set which an element will belong to, this is done when initialising the structure and the elements that
    will belong to it.

        - add_set(v): this will add a set {v} to the forest of disjoint sets
        - union_sets(a, b): this will combine the sets that contain a and b, into a single set.
        - find_set(v): this will find the set to which v belongs, given by the root/representative

        All these operations are done in O(1) time average. There are alternative structures to this DSU that are
        considered more powerful, but have a worse average time of O(logn).

    Structure:
        - We store each set as a tree, where the root is the representative of the set.
        - When we add_set(v), we will simply add a new tree to the forest, with root being v and the
        parent/representative of v being v itself, this indicates it is the root.
        - When doing union_sets(a, b), we must find the representative of both a and b, if they are the same, then the
        sets are already merged, else we simply decide which representative to use as the root of both.
        - The find_set(v) method will simply climb the tree until we find the representative of the  set, ie the
        element who's parent is itself.


    Optimizations:

        Path Compression:
            - By simply making one set attach itself onto the other in order to Union them, we can very quickly end up
            with skewed trees whos traversal would take O(n) time when calling the find_set operation.
            - To fix this, we compress the set while traversing it. When traversing from some element v up to its
            representative p, we set the parent of each node traversed to p.
           - This simple implementation achieves a time of O(logn) on average.

        Union by size/rank:
            - This uses some conditional in order to choose which set has its representative changed. This will prevent
            skewed trees from forming.
            - One possible way is to use the size of the tree, the one with the smaller size gets attached to the one
            with a larger size.


"""


class DSU:

    def __init__(self):
        self.elements = {}

    def add_set(self, v):
        if not self.elements.get(v):
            self.elements[v] = [v, 1]

    def find_set(self, v):
        if self.elements[v][0] == v:
            return self.elements[v][0]
        else:
            self.elements[v][0] = self.find_set(self.elements[v][0])  # Path compression
        return self.elements[v][0]

    def union_sets(self, a, b):
        rep_a = self.find_set(a)
        rep_b = self.find_set(b)
        if rep_a != rep_b:
            if self.elements[rep_a][1] < self.elements[rep_b][1]:  # Union by rank
                rep_a, rep_b = rep_b, rep_a
            self.elements[rep_b][0] = rep_a
            self.elements[rep_a][1] += self.elements[rep_b][1]


def example():
    v = [1, 2, 3, 4, 5, 6, 7, 8]
    s = DSU()
    for i in v:
        s.add_set(i)
    print("----- Insert elements [1, 2, 3, 4, 5, 6, 7, 8] into disjoint sets -----")
    print(s.elements)
    print("----- Perform Union(1, 2) -----")
    s.union_sets(1, 2)
    print(s.elements)
    print("----- Perform Union(3, 4) -----")
    s.union_sets(3, 4)
    print(s.elements)
    print("----- Perform Union(5, 1) -----")
    s.union_sets(5, 2)
    print(s.elements)
    print("----- Perform Union(5, 4) -----")
    s.union_sets(5, 4)
    print(s.elements)

