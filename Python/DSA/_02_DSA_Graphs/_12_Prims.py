"""
Like Kruskal's, Primm's is a generic minimum spanning tree algorithm, however, as we add edges to our solution subset,
the edges in the solution will always form a single tree, whereas Kruskal's could have formed a forest of trees. This
is achieved by adding only the lightest edges to the solution that can be reached from the current solution. The
algorithm therefor will require the input graph, and a starting vertex, we can then add/relax the edge weights as we
add more edges to our solution.

Implementation:
    - For all vertices, we initialise their minimum weight edge that connects them to the solution tree as +inf, and
    starting vertex as 0. Create a structure to keep track of the predecessor mapping of each vertex.
    - Add all vertices to a min Priority Queue based on their minimum weighted edge from the tree.
    - While the Queue is not empty,
        - Extract min, u
        - For all adjacent vertices to u, v, if v is unvisited and the edge (u, v) is less than the current minimum
        weighted edge of v to the tree, then add this edges to our predecessor mapping and update the new minimum key
        value of v in the min priority queue.


The running time is O(VlogV + ElogV) (when using adjacency list)

"""
import heapq
from _02_AdjacencyMatrix import AdjMatrix


def primms(graph, start):
    # Initialise Structures
    distance = {}
    path = {}
    q = []
    for u in graph.get_vertices():
        distance[u] = float("inf")
        path[u] = None
    distance[start] = 0
    # Add to min heap
    for k, v in distance.items():
        heapq.heappush(q, (v, k))
    # Execution
    visited = set()
    while q:
        vertex = heapq.heappop(q)
        if vertex[0] == float("inf"):
            return path
        u = vertex[1]
        if u not in visited:
            visited.add(u)
            for v in graph.get_adj_vertices(u):
                temp = graph.get_edge(u, v)
                if v not in visited and temp < distance[v]:
                    path[v] = u
                    distance[v] = temp
                    heapq.heappush(q, (temp, v))
    return path


"""
NOTE: in our implementation we are simply pushing the new updated distance as another item into the min heap, this 
is because there is no update key capabilities. We can deal with this by ending the process early when we extract 
a vertex with distance inf. At this point, all valid keys will have been added to the solution path, and the remaining 
items in the min heap will be those that were already "updated".
"""


def example():
    edges = [(1, 2, 4),
             (1, 3, 8),
             (2, 3, 11),
             (2, 4, 8),
             (3, 5, 7),
             (3, 6, 1),
             (4, 5, 2),
             (4, 7, 7),
             (4, 8, 4),
             (5, 6, 6),
             (6, 8, 2),
             (7, 8, 14),
             (7, 9, 9),
             (8, 9, 10)]
    g = AdjMatrix(directed=False)
    for e in edges:
        g.add_edge(e[0], e[1], e[2])
    g.show()
    path = primms(g, 1)
    print(path)

example()

