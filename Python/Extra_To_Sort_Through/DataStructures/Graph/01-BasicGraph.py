"""
Overview: https://www.programiz.com/dsa/graph

    Graph data structures are a collection of nodes that contain data and are connect to
    other nodes, given by (V,E):
        - V is a collection of vertices
        - E is a collection of edges, represented by ordered pairs of vertices (u,v)

    Terminology:
        - A vertex is adjacent to another if there is an edge connecting them
        - A path is a sequence of edges to go from one vertex to another
        - Directed Graph is when (u,v) != (v,u), edges have direction


Graph Representation:

    Adjacency Matrix:
        - A 2D array of VxV, if a[i][j]=_01_BasicPython then there is an edge from vertex i to j.
        - Note if graph is undirected then a[i][j] = a[j][i], symmetric along diagonal.
        - Looking up edges is very fast, however we must use massive arrays to cover
        every possible edge.

    Adjacency List:
        - Represents a graph as an array of linked lists.
        - The index of the array represents the vertex and each
        element in the linked list represents a vertex that forms an edge with the index
        vertex.
        - Advantage of this is smaller storage, as we only have to store values that
        form an edge with the index vertex.


Graph is undirected if edges don't point in any direction, and is connected if there is
always a path a vertex to any other vertex.

    Spanning Tree:
        - This is a sub-graph of an undirected connected graph, it includes all the
        vertices of the graph with a minimum possible number of edges. If a vertex
        is missed then it is not a spanning tree.
        - The total number of spanning trees with n vertices that can be created from
        a graph is n**(n-2).

    Minimum Spanning Tree:
        - This is a spanning tree in which the weighted sum of the edges is a minimum.


A strongly connected component is a portion of a directed graph where there is a path
from each vertx to another, check SCC.py

"""

