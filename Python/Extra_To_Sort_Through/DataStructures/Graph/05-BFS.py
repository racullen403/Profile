"""
Breadth First Search:

    Very similar idea to DFS:
        - Add a vertex to the back of a queue.
        - Take item at front of queue and add to visited list.
        - Add its adjacent vertex nodes, which haven't been visited, to the back of the queue (DFS would have been front
        using a stack).
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

print("Using Sets")
graph = {'0': {'_01_BasicPython', '2', '3'},
         '_01_BasicPython': {'0', '2'},
         '2': {'0', '_01_BasicPython', '4'},
         '3': {'0'},
         '4': {'2'}}

print(bfs_with_sets(graph, root='0'))


# using lists instead of sets retains the order of the values in the dictionary/graph
def bfs_with_lists(graph, root):

    visited = []
    queue = deque([root])

    while queue:
        v = queue.popleft()
        print("Visiting Vertex " + str(v))
        visited.append(v)
        for adj_v in graph[v]:
            if adj_v not in visited and adj_v not in queue:
                queue.append(adj_v)
    return visited


print("\nUsing lists")
graph = {'0': ['_01_BasicPython', '2', '3'],
         '_01_BasicPython': ['0', '2'],
         '2': ['0', '_01_BasicPython', '4'],
         '3': ['0'],
         '4': ['2']}

print(bfs_with_lists(graph, root='0'))