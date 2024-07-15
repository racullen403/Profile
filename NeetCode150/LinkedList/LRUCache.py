"""
Medium: Implement Least Recently Used cache of size 'capacity', It should be able to get the value for a key using 'get' method and 
should be able to update/add value of a key using 'put' method. If adding a new key causes capacity limit to be exceeded, remove the LRU key. 
We say a key is used if the get/put method is called on it. Get and Put should run in O(1) average time.

Sol:
    - We implement this as a linked list as we can easily insert and remove in O(1) time, and find the LRU term.
    
        Initialise as (LEFT) <---> (RIGHT) as or list

        If we want to insert, we do so to the left of (RIGHT)
        If we reach capacity we remove the node to the right of (LEFT)
        
        When removing we just consider the nodes left and right of the node to be deleted, and make all their pointers point to eachother. 

        Update cache as required (only when deleting or adding nodes, not when updating/getting)
        
"""
class ListNode:

    def __init__(self, key=0, val=0,):
        self.key = key 
        self.val = val
        self.next = None
        self.prev = None
    

class LRUCache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}         # {key: node}
        self.left = ListNode()
        self.right = ListNode()
        self.left.next = self.right 
        self.right.prev = self.left      # (0:0) <---> (0:0) initialised
        
    def remove(self, node):
        l, r = node.prev, node.next 
        l.next = r 
        r .prev = l

    def insert(self, node):
        l, r = self.right.prev, self.right 
        node.prev = l 
        node.next = r 
        l.next = node 
        r.prev = node 

    def get(self, key):
        if key not in self.cache:
            return - 1
        self.remove(self.cache[key])
        self.insert(self.cache[key])
        return self.cache[key].val
        
    
    def put(self, key, value):
        if key in self.cache:
            self.remove(self.cache[key])
            del self.cache[key]
        if len(self.cache) == self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        node = ListNode(key, value)
        self.insert(node)
        self.cache[key] = node
        

        