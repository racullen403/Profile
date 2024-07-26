"""
Medium: Given a connected undirected graph, return a deep copy of it. Each node counts an int value and a list of neighbours.
Graph will we given as an Adjacency List.

Sol:
    - DFS through to create all the required nodes.
    - Map oldNodes: newNodes, as we dfs the neighbours, return the new result once it is in our map, else keep exploring.
    - In doing so, we create a copy of the node, add it to a map, and explore its neighbours, this process continues in a DFS until a node is fully explored,
    ie, all the neighbour nodes are created, in which case we return the created nodes.
"""

class Node():

    def __init__(self, val = 0, neighbours = None):
        self.val = val 
        self.neighbors = [] if neighbours is None else neighbours

    
def cloneGraph(node):
    nodes = {}  # {old node: new node}

    def backtrack(node):
        if node in nodes:       # node we are exploring has already been created, return it
            return nodes[node]
        new = Node(node.val)    # New copy node
        nodes[node] = new       # Add it to oldNode: newNode
        for neigh in node.neighbors:
            new.neighbors.append(backtrack(neigh))  # For each neighbour, if copy exists in the map then we append it, else create it, add to map, and explore its neighbours.
        return new  # Once done, return the completed node
    
    return None if not node else backtrack(node)
