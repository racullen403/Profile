"""
Depth First Search:

    DFS is an algorithm for traversing all the vertices of a graph or tree structure. The standard approach is to
    categorise all the vertices as being either visited or not_visited.

    We try to visit all the vertices while avoiding an endless cycle.

    Implementation:
        - Put any vertex into the top of a stack
        - Pop from the stack and "explore" the vertex, adding the vertex to the visited list, and its adjacent vertices
        that haven't been visited into the stack.
        - Repeat this last step until the stack is empty

    Note this works for a connected graph if we run it once, for a disconnected graph we run
    it on every node to ensure we visit all nodes.

    Complexity:
        - Time complexity is O(V+E)
        - Space complexity is O(V)
"""


def dfs_with_sets(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    # For vertices in linked list (not including nodes already visited), apply DFS
    for adj_vertex in graph[start]:
        if adj_vertex not in visited:
            dfs_with_sets(graph, adj_vertex, visited)
    return


# Non-Recursive DFS
def dfs_non_recursive(graph, start):
    visited = set()
    stack = [start]
    while stack:
        vertex = stack.pop()
        visited.add(vertex)
        print("Visiting Vertex: " + str(vertex))
        for adj_v in graph[vertex]:
            if adj_v not in visited:
                stack.append(adj_v)
    return


def adj_matrix_dfs(graph):
    stack = []
    visited = set()
    vertex = graph.get_vertex()  # Made up method for getting the first vertex
    stack.append(vertex)
    while len(stack) > 0:
        v = stack.pop()
        visited.add(v)
        for u in graph[v].keys():
            if graph[v][u] != 0 and u not in visited:
                stack.append(u)


def adj_list_dfs(graph):
    stack = []
    visited = set()
    vertex = graph.get_vertex()
    stack.append(vertex)
    while len(stack) > 0:
        v = stack.pop()
        visited.add(v)
        edge = v.edges
        while edge:  # Made up methods for traversing the linked list of edges for some vertex v
            if edge not in visited:
                stack.append(edge)
            edge = edge.next