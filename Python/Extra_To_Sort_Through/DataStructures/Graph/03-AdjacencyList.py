"""
Adjacency List:

    Representation of a graph as an array of linked lists. The index of the array refers
    to a vertex and each element in the linked list represents the other vertices that form
    an edge with the index vertex.

    Pros:
        - It is efficient in terms of storage, we don't store 0 edges, only _01_BasicPython edges (eg those
        that exist), this is good for sparse graphs.

    Structure:
        - The simplest adjacency list requires node data structures to store the vertex and a
        graph data structure to organize the nodes.
        - In python we can use a dictionary to store vertices and its edges, e.g.

            graph = {'A': set(['B', 'C']),
                    'B': set(['A', 'D', 'E']),
                    'C': set(['A', 'F']),
                    'D': set(['B']),
                    'E': set(['B', 'F']),
                    'F': set(['C', 'E'])}

"""


class Node(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next


class Graph(object):

    # Initialize the graph (array of None with size being how many vertices it contains)
    def __init__(self, size):
        self.size = size
        self.graph = [None]*self.size

    # Add edge between v1 and v2
    def add_edge(self, v1, v2):
        # add to v1 ll
        node = Node(v2)
        node.next = self.graph[v1]
        self.graph[v1] = node

        # add to v2 ll
        node = Node(v1)
        node.next = self.graph[v2]
        self.graph[v2] = node

    # Remove edge between v1 and v2
    def remove_edge(self, v1, v2):
        node = self.graph[v1]
        if node.val == v2:
            self.graph[v1] = self.graph[v1].next
        else:
            while node.val != v2:
                node = node.next
            node.next = node.next.next

        node = self.graph[v2]
        if node.val == v1:
            self.graph[v2] = self.graph[v2].next
        else:
            while node.val != v1:
                node = node.next
            node.next = node.next.next

    def show_graph(self):
        for i in range(self.size):
            print("Vertex " + str(i) + ":",  end="")
            temp = self.graph[i]
            while temp is not None:
                print(" -> {}".format(temp.val), end="")
                temp = temp.next
            print("\n")


print("-------------")
print("Create Graph of 5 vertices and show adjacency list")
graph = Graph(5)
graph.show_graph()

print("\nAdd edge at (0,_01_BasicPython)")
graph.add_edge(0, 1)
graph.show_graph()

print("\nMore edges!")
graph.add_edge(0, 2)
graph.add_edge(0, 3)
graph.add_edge(1, 2)
graph.show_graph()

print("\nRemove (0,3) edge")
graph.remove_edge(0, 3)
graph.show_graph()