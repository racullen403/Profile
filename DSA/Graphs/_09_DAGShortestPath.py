"""
We can relax the edges of a weighted DAG according to the topological sorting of its vertices, in doing so, we can
compute the shortest paths from a single source in O(V+E) time. This is because a DAG does not contain any cycles and
so it is well-defined.

Implementation:
    - Topologically sort the vertices of the dag (if edge (u, v) exists, then u will always come before v in the
     sorted list).
    - Initialise our single source, ie set all distances from s to +inf and distance from s as 0, and set up the
    predecessor path.
    - In topological order, take each vertex v and for its adjacent vertices u, relax the distance to u from s.

Complexity is O(V + E), this is because the Topological sort is O(V+E), the initialising step is O(V) and the relaxing
of the distances only occurs once per edge meaning the last step is also O(V).

NOTE: log(V+E) is the case for an adjacency list, in an adjacency matrix, we have to check every edge for each vertex,
making it O(V^2).


"""


# Not functional, just example
def dag_shortest_path(g, s):
    # Step 1
    path = topological_sort(g)
    # Step 2
    distance = {}
    predecessor = {}
    for v in g.get_vertices():
        distance[v] = float("inf")
        path[v] = None
    distance[s] = 0
    # Step 3
    for v in path:
        for u in g.get_adj_vertices(v):
            temp = distance[v] + g.get_edge(v, u)
            if temp < distance[u]:
                distance[u] = temp
                predecessor[u] = v