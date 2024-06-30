"""
Dijkstra's Algorithm:

    This is an algorithm for a directed weighted (positive) graph, for finding the shorted path from a starting
    vertex to some other given vertex. It differs from a minimum spanning tree as the shortest path may not include
    all vertices of the graph.

    Implementation:

        - For every vertex in a graph G, assign its distance from starting vertex v0 as +inf. Assign distance for v0
        as 0. Add all vertices into a Priority Queue, Q.

        - While Q is not empty, extract the minimum, v, this will be v0 initially.
            - For every edge from v to some vertex u, if the new distance d(v) + (v,u) is less than the distance
            stored at d(u), then update it and add v as the predecessor of u (this allows us to keep track of the
            path taken).

      The idea of this algorithm is to repeatedly relax the initial distances to some vertex u from the initial vertex
      v0. We use a greedy approach to determine which node we should use to update the distances, this is why a
      Priority Queue is used, as it has logarithmic methods.

    Complexity is O((V+E)logV), We must extract min V times taking VlogV, and for each extract, we must check through
    all the edges E to see if they are updated.

"""


class AdjMatrix:

    def __init__(self, directed=True, positive=True):
        self.graph = {}
        self.vertices = set()
        self.directed = directed
        self.positive = positive

    def add_vertex(self, v):
        if v in self.vertices:
            return
        self.vertices.add(v)
        edges = {v: 0}
        for vertex in self.graph.keys():
            self.graph[vertex][v] = 0
            edges[vertex] = 0
        self.graph[v] = edges

    def add_edge(self, v, u, weight):
        if weight < 0:
            self.positive = False
        if v not in self.vertices:
            self.add_vertex(v)
        if u not in self.vertices:
            self.add_vertex(u)
        self.graph[v][u] = weight
        if not self.directed:
            self.graph[u][v] = weight

    def get_vertices(self):
        vertices = []
        for v in self.vertices:
            vertices.append(v)
        return vertices

    def display(self):
        vertices = self.get_vertices()
        print("----- AdjMatrix -----")
        print("   ", end="")
        for v in vertices:
            print(v, end="  ")
        for i in vertices:
            print()
            print(i, end="  ")
            for j in vertices:
                print(self.graph[i][j], end="  ")
        print()

    def dijkstra_shortest_path(self, s, d):
        if not self.positive:  # If negative weights, we use different method
            return
        vertices = self.get_vertices()
        distance = {}  # Create dictionary of the vertex:distance pairs
        for vertex in vertices:
            distance[vertex] = float("inf")
        distance[s] = 0
        q = PriorityQueue()  # Implement priority queue for queuing vertices based on shortest distance from start
        for vertex in vertices:
            q.insert(vertex, distance[vertex])
        path = {}  # Contains pointers for finding the final path
        visited = set()
        while not q.is_empty():
            v = q.extract_min()
            visited.add(v)
            for u in self.graph[v].keys():
                if self.graph[v][u] != 0 and u not in visited:
                    dist = distance[v] + self.graph[v][u]
                    if dist < distance[u]:
                        distance[u] = dist
                        q.update_key(u, dist)
                        path[u] = v
        stack = []
        while d in path.keys():
            stack.append(d)
            d = path[d]
        stack.append(d)
        path = []
        while stack:
            path.append(stack.pop())
        return path


class PriorityQueue:

    def __init__(self):
        self.q = []
        self.lookup = {}
        self.max = float("inf")

    def is_empty(self):
        return self.q == []

    def insert(self, key, value):
        if value is None:
            value = self.max
        self.q.append(key)
        self.lookup[key] = value
        i = len(self.q) - 1
        self.swim(i)

    def swim(self, index):
        p = (index-1)//2
        if p >= 0 and self.lookup[self.q[index]] < self.lookup[self.q[p]]:
            self.swap(index, p)
            self.swim(p)
        return

    def sink(self, index):
        l = (2*index + 1)
        r = (2*index + 2)
        i = index
        if l <= len(self.q)-1 and self.lookup[self.q[l]] < self.lookup[self.q[i]]:
            i = l
        if r <= len(self.q)-1 and self.lookup[self.q[r]] < self.lookup[self.q[i]]:
            i = r
        if i != index:
            self.swap(index, i)
            self.sink(i)
        return

    def swap(self, i, j):
        self.q[i], self.q[j] = self.q[j], self.q[i]

    def extract_min(self):
        m = self.delete(0)
        return m

    def delete(self, index):
        i = len(self.q)-1
        self.swap(index, i)
        key = self.q.pop()
        self.sink(index)
        return key

    def update_key(self, key, value):
        i = 0
        while i < len(self.q) and self.q[i] != key:
            i += 1
        if i < len(self.q):
            old_value = self.lookup[self.q[i]]
            self.lookup[self.q[i]] = value
            if value < old_value:
                self.swim(i)
            else:
                self.sink(i)


def example():
    g = AdjMatrix()
    edges = [
        (1, 2, 4),
        (1, 3, 4),
        (2, 3, 2),
        (3, 4, 3),
        (3, 6, 1),
        (3, 5, 6),
        (4, 5, 2),
        (6, 5, 3)
    ]
    for e in edges:
        g.add_edge(e[0], e[1], e[2])
    g.display()
    shortest_path = g.dijkstra_shortest_path(1, 5)
    print(shortest_path)



