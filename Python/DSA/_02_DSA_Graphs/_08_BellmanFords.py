"""
Bellman Ford's Algorithm helps to find the shortest path from a vertex to all other
vertices of a weighted graph. It is similar to Dijkstra's but works with negative weighted
edges as it can detect a negative cycle.

Negative edges:
    - They can be used to explain things like cash-flow, heat exchange in chemical
    reactions, etc.
    - We must be careful as they can create negative weight cycles, where a cycle reduces the
    total path distance while also coming back to the same point. This is why a greedy method like Dijkstra's does
    not always work, as it cannot return to an already visited node and reduce it further, it assumes the first time
    the node was visited, it found the optimal path.

Bellman Ford's:
    - Over-estimates the length of the path from the starting vertex to all the other vertices.
    - Similar to Dijkstra's, it will iteratively relax these path distances, however, it does this for every vertex,
    and for every edge from the vertex. This is where is differs, dijkstra's would only relax the path distances for
    nodes that had not yet been visited, whereas BellmanFord may potentially change a node distance V times

Approach:
    - Start with weighted graph
    - Choose a vertex to start at and assign infinity path lengths to all other vertices
    - Visit edges and relax path distance if inaccurate
    - We need to maintain the path distance of every vertex, stored in an array size V.
    - We need to extract the shortest path, map each vertex to the vertex that last updated
    its path length. Once algorithm is over, we can backtrack from destination vertex to
    source and recover the path.

Negative Cycle Detection:
    - https://web.stanford.edu/class/archive/cs/cs161/cs161.1168/lecture14.pdf

Complexity:
    - Time O(VE)
    - Space O(V)

"""
from _02_AdjacencyMatrix import AdjMatrix


def bellman_ford(graph, start):
    distances = {}
    path = {}
    vertices = graph.get_vertices()
    for v in vertices:
        distances[v] = float("inf")
        path[v] = None
    distances[start] = 0
    for v in vertices:  # Update distances for every vertex v and its adjacent vertices u
        for u in graph.get_adj_vertices(v):
            temp = distances[v] + graph.get_edge(v, u)
            if temp < distances[u]:
                distances[u] = temp
                path[u] = v
    for v in vertices:  # Check for negative cycles
        for u in graph.get_adj_vertices(v):
            if distances[v] + graph.get_edge(v, u) < distances[u]:
                print("Negative Cycle Found")
                return
    return path


def example():
    g = AdjMatrix(directed=True)
    edges = [
        (1, 2, 4),
        (1, 3, 4),
        (2, 3, 2),
        (3, 4, 3),
        (3, 6, 1),
        (3, 7, 6),
        (7, 3, 10),
        (4, 5, 2),
        (6, 5, 3)
    ]
    for e in edges:
        g.add_edge(e[0], e[1], e[2])
    g.show()
    shortest_path = bellman_ford(g, 1)
    print(shortest_path)


example()