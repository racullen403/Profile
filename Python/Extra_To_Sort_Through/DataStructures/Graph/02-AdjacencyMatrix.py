"""
Adjacency Matrix:

    This is a way of representing a graph G=(V,E) as a matrix of booleans (0,_01_BasicPython). Its size is
    VxV where V is the number of vertices and the value of Aij is _01_BasicPython or 0 depending in
    whether an edge exists or not for vertex i to vertex j. For undirected graphs the
    matrix is symmetric about the diagonal.

    Pros:
        - Adding/removing edge is time efficient
        - Good for dense graphs with lots of edges, even if graph is sparse we can represent
        it using data structures for sparse matrices.
        - Very powerful GPU's can perform expensixe operations on matrices.

    Cons:
        - The  VxV space requirement is memory intensive.
        - A lot of graphs don't have too many connections making adjacency lists better.
        - While basic operations are easy, trickier ones are very expensive
"""


class Graph(object):

    # Initialise matrix of size by size
    def __init__(self, size, directed=False):
        self.directed = directed
        self.size = size
        self.adjMatrix = []
        for i in range(size):
            self.adjMatrix.append([0 for i in range(size)])

    # Add Edge between v1 and v2
    def add_edge(self, v1, v2):
        if v1 == v2:
            print("No can do!")
            return
        if self.directed is False:
            self.adjMatrix[v1][v2] = 1
            self.adjMatrix[v2][v1] = 1
        else:
            self.adjMatrix[v1][v2] = 1

    def remove_edge(self, v1, v2):
        if v1 == v2:
            print("No can do!")
            return
        if self.directed is False:
            self.adjMatrix[v1][v2] = 0
            self.adjMatrix[v2][v1] = 0
        else:
            self.adjMatrix[v1][v2] = 0

    def show_matrix(self):
        print("----------")
        print("MATRIX:")
        for i in self.adjMatrix:
            print(i)
        print("----------")

a = Graph(size=5)
print("Show graph")
a.show_matrix()
print("Add edges")
a.add_edge(0, 1)
a.add_edge(0, 2)
a.add_edge(1, 2)
a.add_edge(2, 0)
a.add_edge(2, 3)
a.show_matrix()
print("Remove edge (0,_01_BasicPython)")
a.remove_edge(0, 1)
a.show_matrix()