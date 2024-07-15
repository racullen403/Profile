class Node:

    def __init__(self, val):
        self.val = val
        self.next = None
        self.random = None


def copyRandomList(head):
    """
    Medium: Given linked list length n, with additional random pointer that points to any node in the list or None. Create a deep copy of list, ie new list should 
    not have any pointers to nodes in head.

    Sol: 
        - Iterate through list, creating every node needed and storing in a hashmap, oldNode: newNode, this way if their are duplivacate values, we can double check.
        - Do a second pass of the original, connecting the pointers for the new using the hashmap.

    """
    lookup = {}
    temp = head
    while temp:
        node = Node(temp.val)
        lookup[temp] = node 
        temp = temp.next
    lookup[None] = None

    temp = head
    while temp:
        node = lookup[temp]
        node.next = lookup[temp.next]
        node.random = lookup[temp.random]
        temp = temp.next
    
    return lookup[head]