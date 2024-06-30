"""
Topological Sort:

    We can use a DFS on a directed acyclic graph (dag) to perform a Topological Sort. This is a liner ordering of
    vertices v in a graph G, such that if an edge (u, v) exists, then u will appear before v in the ordering. This is
    why the graph must be a dag, any cycles will prevent a linear ordering.

    We can think of this as placing all vertices on a horizontal line, and all their edges must point from left to
    right.

    Procedure:

        - DFS(G), computing finish times of verices v as v.f
        - As each vertex finishes, insert it into the front of a linked list
        - The final linked list will form the topologically sorted vertices

    DAG:
        We can tell if a graph is acyclic if it does not contain a back edge in the DFS. A back edge is (u, v) such
        that v is an ancestor of u.

    Complexity is O(V + E) since that is the complexity of a DFS.
"""


def topological_sort(graph):
    output = []
    visited = set()
    to_visit = graph.get_vertices()

    def dfs():
        v = to_visit.pop()
        if v not in visited:
            visited.add(v)
            for u in graph.get_adj_vertices(v):
                if u not in visited:
                    to_visit.append(u)
                    dfs()
            output.append(v)

    while to_visit:
        dfs()

    output.reverse()
    return output


def example():
    from _02_AdjacencyMatrix import AdjMatrix
    g = AdjMatrix(directed=True)
    e = [(0, 1),
         (0, 6),
         (1, 4),
         (1, 2),
         (2, 3),
         (2, 4),
         (4, 6),
         (4, 5),
         (6, 5)]
    for edge in e:
        g.add_edge(edge[0], edge[1])
    g.show()
    print(topological_sort(g))


example()