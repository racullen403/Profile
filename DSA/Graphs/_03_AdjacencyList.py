"""
Adjacency List:

    Representation of a graph as an array of linked lists. We contain every vertex in some list, and a pointer from
    each vertex to another list that contains the vertices it has edges with.

    Pros:
        - It is efficient in terms of storage, we don't store 0 edges, this is good for sparse graphs.

    Structure:
        - The simplest adjacency list requires node data structures to store the vertex and a
        graph data structure to organize the nodes.
        - In python we can use a dictionary to store vertices and its edges, e.g. A set of the connected vertices
        also allows very fast look up times.

            graph = {'A': set(['B', 'C']),
                    'B': set(['A', 'D', 'E']),
                    'C': set(['A', 'F']),
                    'D': set(['B']),
                    'E': set(['B', 'F']),
                    'F': set(['C', 'E'])}

"""


class AdjList:

    def __init__(self, directed=False):
        self.graph = {}
        self.vertices = set()
        self.is_directed = directed
        self.is_positive = True

    def add_vertex(self, v):
        if v in self.vertices:
            return
        else:
            self.graph[v] = set()
            self.vertices.add(v)

    def add_edge(self, v, u, weight=1):
        if v not in self.vertices:
            self.add_vertex(v)
        if u not in self.vertices:
            self.add_vertex(u)
        self.graph[v].add((u, weight))
        if not self.is_directed:
            self.graph[u].add((v, weight))

    def get_graph(self):
        return self.graph

    def get_transpose(self):
        t = AdjList(self.is_directed)
        for v in self.vertices:
            for u in self.graph[v]:
                t.add_edge(u[0], v, u[1])
        return t

    def show(self):
        print(self.graph)


# Example of inserting Vertices + Edges + Edge without predefined vertex "D"
def example1():
    g = AdjList()
    for v in ["A", "B", "C"]:
        g.add_vertex(v)
    print("----- Insert Vertices without edges -----")
    g.show()
    print("-----Add Edges for undirected graph -----")
    edges = [("A", "B"), ("B", "C"), ("C", "A"), ("C", "D")]
    for e in edges:
        g.add_edge(e[0], e[1])
    g.show()


# Example of transpose
def example2():
    g = AdjList(True)
    for v in ["A", "B", "C"]:
        g.add_vertex(v)
    print("----- Insert Vertices without edges -----")
    g.show()
    print("-----Add Edges for directed graph -----")
    edges = [("A", "B"), ("B", "C"), ("C", "A"), ("C", "D")]
    for e in edges:
        g.add_edge(e[0], e[1])
    g.show()
    print("----- Get Transpose -----")
    t = g.get_transpose()
    t.show()


