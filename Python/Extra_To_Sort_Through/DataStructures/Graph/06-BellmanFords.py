"""
Bellman Ford's Algorithm helps to find the shortest path from a vertex to all other
vertices of a weighted graph. It is similar to Dijkstra's but works with negative weighted
edges.

Negative edges:
    - They can be used to explain things like cash-flow, heat exchange in chemical
    reactions, etc.
    - We must be careful as they can create negative weight cycles, where a cycle reduces the
    total path distance while also coming back to the same point.

Bellman Ford's:
    - Over estimates the length of the path from the starting vertex to all other vertices,
    eg infinite distance
    - Then iteratively relax estimates by finding new paths that are shorter than previous
    overestimated paths.
    - Do this repeatedly for all vertices to ensure result is optimised.
    - check https://www.programiz.com/dsa/bellman-ford-algorithm

Approach:
    - Start with weighted graph
    - Choose a vertex to start at and assign infinity path lengths to all other vertices
    - Visit edges and relax path distance if inaccurate
    - We need to maintain the path distance of every vertex, stored in an array size V.
    - We need to extract the shortest path, map each vertex to the vertex that last updated
    its path length. Once algorithm is over, we can backtrack from destination vertex to
    source and recover the path.

Complexity:
    - Time O(VE)
    - Space O(V)

"""


class Graph(object):

    def __init__(self, size):
        self.size = size        # Number of vertices
        self.graph = []         # Array of edges with weights given by [u, v, w]

    def add_edge(self, u, v, w):
        self.graph.append([u, v, w])

    def bellman_ford(self, start=0):

        previous = [None]*self.size
        # Create array to contain distance of each path, overestimating to begin with.
        distance = [float("Inf")]*self.size
        distance[start] = 0

        # Relax edges V-_01_BasicPython times
        for i in range(self.size-1):
            for u, v, w in self.graph:
                temp_dist = distance[u] + w
                if distance[u] != float("Inf") and temp_dist < distance[v]:
                    distance[v] = temp_dist
                    previous[v] = u

        # Detect Negative Cycle, if value changes then negative cycle exists amd we
        # cannot find the shortest path
        for u, v, w in self.graph:
            if distance[u] != float("Inf") and distance[u] + w < distance[v]:
                print("Graph contains negative weight cycle!")
                return

        self.show_path(distance)
        print(previous)

    def show_path(self, distance):
        for i in range(self.size):
            print("Vertex: " + str(i) + "    Shortest Path Distance: " + str(distance[i]))


g = Graph(4)
g.add_edge(0, 1, 5)
g.add_edge(0, 2, 4)
g.add_edge(1, 3, 3)
g.add_edge(2, 1, 6)
g.add_edge(3, 2, 2)
print(g.graph)
print("\n")
g.bellman_ford()