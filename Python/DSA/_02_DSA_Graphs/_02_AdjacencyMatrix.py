"""
Adjacency Matrix:

    This is a way of representing a graph G=(V,E) as a matrix of weights. Its size is
    VxV where V is the number of vertices and the value of Aij is the weight of the edge between vertex i and vertex
    j (no edge is 0).  For undirected graphs the matrix is symmetric about the diagonal. Aij == Aji

    Pros:
        - Adding/removing/searching for an edge is time efficient
        - Good for dense graphs with lots of edges. When the graph is sparse we can represent it using data structures
        for sparse matrices.
        - Very powerful GPU's can perform expensive operations on matrices.

    Cons:
        - The  VxV space requirement is memory intensive.
        - A lot of graphs don't have too many connections making adjacency lists better.
        - While basic operations are easy, trickier ones are very expensive

"""


class AdjMatrix:

    def __init__(self, directed=False):
        self.graph = {}
        self.vertices = set()
        self.is_directed = directed
        self.is_positive = True  # Lets us know if there are negative weights

    def add_vertex(self, v):
        if v in self.vertices:
            return
        else:
            new_vertices = {v: 0}
            for vertex in self.vertices:
                self.graph[vertex][v] = 0  # Add a 0 edge from all vertices to the new one
                new_vertices[vertex] = 0  # Add a 0 edge from the new vertex to all existing vertices
            self.graph[v] = new_vertices  # Add this new vertex to the matrix
            self.vertices.add(v)

    def add_edge(self, u, v, weight=1):
        if weight < 0:
            self.is_positive = False
        if u not in self.vertices:
            self.add_vertex(u)
        if v not in self.vertices:
            self.add_vertex(v)
        self.graph[u][v] = weight
        if not self.is_directed:
            self.graph[v][u] = weight

    def get_graph(self):
        return self.graph

    def get_vertices(self):
        return [v for v in self.vertices]

    def get_edge(self, v, u):
        return self.graph[v][u]

    def get_adj_vertices(self, v):
        output = []
        for u in self.get_vertices():
            if self.graph[v][u] != 0:
                output.append(u)
        return output

    def get_transpose(self):
        v = []
        t = AdjMatrix(directed=self.is_directed)
        for u in self.vertices:
            v.append(u)
            t.add_vertex(u)
        for i in range(len(v)):
            for j in range(i, len(v)):
                t.add_edge(v[i], v[j], self.graph[v[j]][v[i]])
                t.add_edge(v[j], v[i], self.graph[v[i]][v[j]])
        return t

    def show(self):
        print("\n-------- Graph --------")
        vertices = [v for v in self.vertices]
        print("   ", end=" ")
        for i in vertices:
            print(i, end="  ")
        print()
        for v in vertices:
            print(" ", v, end=" ")
            for u in vertices:
                print(self.graph[v][u], end="  ")
            print()


# Example inserting Vertices
def example1():
    g = AdjMatrix()
    for v in ["A", "B", "C"]:
        g.add_vertex(v)
    g.show()


# Example of inserting edges
def example2():
    g = AdjMatrix(directed=True)
    edges = [("A", "B", 1), ("B", "C", 5), ("C", "A", 3)]
    for i in edges:
        g.add_edge(i[0], i[1], i[2])
    g.show()


# Example Graph + Transpose Graph
def example3():
    e = [(1, 2), (2, 3), (3, 4), (4, 1), (3, 5), (5, 6), (6, 7), (7, 5), (7, 8)]
    g = AdjMatrix(directed=True)
    for v in e:
        g.add_edge(v[0], v[1])
    g.show()
    t = g.get_transpose()
    t.show()
