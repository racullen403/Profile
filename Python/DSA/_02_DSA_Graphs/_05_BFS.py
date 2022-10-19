"""
Breadth First Search:

    Given some graph, G={V,E}, BFS will explore it in a "radial" approach, exploring vertices in order of their
    distance (radius) from the starting node. It can be useful to keep track of the entry and finish times when
    exploring nodes, this can give us more insight into the relationships between nodes.

    Very similar idea to DFS, however we use a queue to store the next vertex to visit, rather than a stack:
        - Add a vertex to the back of a queue.
        - Take item at front of queue and add to visited list.
        - Add its adjacent vertex nodes, which haven't been visited, to the back of the queue (DFS would have added to
        the front of the queue using a stack).
        - Repeat until queue is empty

    Complexity:
        - Time O(V+E)
        - Space O(V)
"""

# Best implementation of the queue is to use a deque from collections
from collections import deque


def bfs_with_sets(graph, root):
    visited = set()
    queue = deque([root])
    while queue:
        v = queue.popleft()
        print("Visiting Vertex " + str(v))
        visited.add(v)
        for adj_v in graph[v]:
            if adj_v not in visited and adj_v not in queue:
                queue.append(adj_v)
    return visited


def adj_matrix_bfs(graph):
    visited = set()
    queue = []
    pos = 0
    vertex = graph.get_vertex()  # Made up method to get first vertex
    queue.append(vertex)
    while pos < len(queue):
        v = queue[pos]
        visited.add(v)
        for u in graph[v].keys():
            if graph[v][u] != 0 and graph[v][u] not in visited:
                queue.append(u)
        pos += 1

