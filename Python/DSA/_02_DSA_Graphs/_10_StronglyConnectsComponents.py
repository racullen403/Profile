"""
Strongly Connected Components:

    A Strongly Connected Component of a directed graph G=(V,E) is a subset of vertices C such that for every pair of
    vertices u, v in C, there exists a path (u,v) and (v,u).

    One of the use cases of DFS is to decompose a graph into its SCC's, we do this by applying DFS on G, and then
    again applying a DFS but on the transpose graph of G. By obtaining the SCC's of G, we can run other procedures on
    the components separately and combine the solutions.

    It is interesting to note that the SCC of G will be the same SCC of the transpose graph. Hence, u and v are
    reachable in G if and only if they are reachable in the transpose of G.


    Procedure for finding SCC of G:
        - Call DFS on G to find the topologically ordered vertices (increasing finish times of vertices).
        - Compute the transpose of G, T.
        - Call DFS on T, but consider the vertices in order of decreasing finish times (found in first step).
        Output the vertices from each tree in the depth first forest as their own SCC.

    The idea behind this procedure comes from the property of the component graph:
        Let C1, C2, ..., Cn be the SCC on some graph G. Then there exists a vertex vi for each Ci that form the
        vertex set Vscc. We say the component graph Gscc = (Vscc, Escc) where Escc=(vi,vj) and vi,vj belong to Vscc.

        The component graph, Gscc is a DAG.

    Complexity, when using adjacency lists is O(V+E)
"""
from _02_AdjacencyMatrix import AdjMatrix


def dfs_get_path(graph, vertex, visited, path):
    visited.add(vertex)
    for u in graph.get_adj_vertices(vertex):
        if u not in visited:
            dfs_get_path(graph, u, visited, path)
    path.append(vertex)


def dfs_get_components(graph, vertex, visited, component):
    component.append(vertex)
    visited.add(vertex)
    for u in graph.get_adj_vertices(vertex):
        if u not in visited:
            dfs_get_components(graph, u, visited, component)


def kosaraju_scc(graph):
    visited = set()
    stack = []
    for v in graph.get_vertices():  # Step 1
        if v not in visited:
            dfs_get_path(graph, v, visited, stack)
    assigned = set()
    t = graph.get_transpose()
    root = 1
    scc = {}
    component = []
    while stack:  # Step 2
        v = stack.pop()
        if v not in assigned:
            dfs_get_components(t, v, assigned, component)
            scc[root] = component
            root += 1
            component = []
    return scc


def example():
    g = AdjMatrix(directed=True)
    edges = [(1, 2),
             (1, 4),
             (2, 3),
             (2, 5),
             (3, 1),
             (4, 3),
             (5, 8),
             (5, 6),
             (6, 9),
             (6, 7),
             (7, 5)]
    for e in edges:
        g.add_edge(e[0], e[1])
    g.show()
    scc = kosaraju_scc(g)
    print("Strongly Connect Components:", scc)


