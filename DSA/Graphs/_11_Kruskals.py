"""
Kruskal's Algorithm:

    This is a minimum spanning tree algorithm, it takes a graph a returns a subset of all the edges that which form a
    tree containing all the vertices of the graph while maintaining the minimum summed weight of all the edges.

    Kruskal's is a greedy algorithm that finds the locally optimal solution, in the hopes that it will lead to the
    optimal solution.

    In Kruskal's, the set A is a forest of the vertices given by a graph G. The safe edge that will be added to A is
    the least-weight edge that connects two distinct components.

    Procedure:
        - Sort all the edges into order of the lowest weight to the highest.
        - Take the lowest weight edge and add it to our solution, if it creates a cycle, remove it.
        - Continue on until we have reached all vertices.

    Note that a common way to find if adding an edge would cause a cycle is to use the Disjoint Set Union data
    structure, if vertices v and u already exist in the same set, then the edge (u,v) or (v, u) would cause a cycle.
    This can be found by using find_set(u) and find_set(v), if they return the same representative element, then v and
    u belong to the same set and (u, v) is forms a cycle.

    Complexity is O(ElogV)
"""


def kruskal(graph):
    s = DSU()
    for v in graph:
        s.add_set(v)
    edges = graph.sort_by_increasing_edge_weight()
    mst = []
    for (u, v) in edges:
        if s.find_set(u) != s.find_set(v):
            s.union_sets(u, v)
            mst.append((u, v))
    return mst

