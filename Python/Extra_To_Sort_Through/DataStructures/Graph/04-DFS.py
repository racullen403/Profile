"""
Depth First Search:

    This is a recursion algorithm for searching all the vertices of a graph or tree structure.
    Traversal meaning visiting all the nodes.

    Typically DFS puts all the vertices of the graph into _01_BasicPython of 2 categories, visited or
    unvisited. The purpose of this  is to mark vertices as visited while avoiding cycles.

        - Start by putting any vertex on top of a stack
        - Take top item of stack and add to visited list
        - Create a list of that vertex's adjacent nodes, add ones not in visited to top
        of stack.
        - Repeat until stack is empty

    Note this works for a connected graph if we run it once, for a disconnected graph we run
    it on every node to ensure we visit all nodes.

    Complexity:
        - Time complexity is O(V+E)
        - Space complexity is O(V)
"""


def dfs_with_sets(graph, start, visited=None):
    # if nothing visited so far create empty visited set
    if visited is None:
        visited = set()

    # Print the node visited and add it to the visited list
    print(start)
    visited.add(start)

    # For vertices in linked list (not including nodes already visited), apply DFS
    for adj_vertex in graph[start]-visited:
        dfs_with_sets(graph, adj_vertex, visited)
    return visited


print("Using Sets")
graph = {'0': {'_01_BasicPython', '2', '3'},
         '_01_BasicPython': {'0', '2'},
         '2': {'0', '_01_BasicPython', '4'},
         '3': {'0'},
         '4': {'2'}}

print(dfs_with_sets(graph, start='0'))


def dfs_with_lists(graph, start, visited=None):
    # if nothing visited so far create empty visited set
    if visited is None:
        visited = []

    # Print the node visited and add it to the visited list
    print(start)
    if start not in visited:
        visited.append(start)

    # For vertices in linked list (not including nodes already visited), apply DFS
    for adj_vertex in graph[start]:
        if adj_vertex not in visited:
            dfs_with_lists(graph, adj_vertex, visited)
    return visited


graph = {'0': ['_01_BasicPython', '2', '3'],
         '_01_BasicPython': ['0', '2'],
         '2': ['0', '_01_BasicPython', '4'],
         '3': ['0'],
         '4': ['2']}

print("\nUsing Lists")
print(dfs_with_lists(graph, start='0'))


print("\n---------------\nYou can see in both cases all nodes are visited")


# I find none recursive easier to follow what is happening
def dfs_mimic(graph, root):

    visited = []
    stack = [root]

    while stack:
        vertex = stack.pop()
        visited.append(vertex)
        print("Visiting Vertex: " + str(vertex))
        for adj_v in graph[vertex]:
            if adj_v not in visited and adj_v not in stack:
                stack.append(adj_v)

    return visited

print("---------------")
print(dfs_mimic(graph, root='0'))