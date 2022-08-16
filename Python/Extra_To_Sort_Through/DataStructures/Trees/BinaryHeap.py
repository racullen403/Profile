"""
A Heap Data Structure is a complete binary tree that satisfies the heap property (we can think of the
binary heap as a priority queue):

    Complete Binary Tree:
        - All levels except the last are filled
        - All nodes in the last level fill from the left
        - These trees are balanced, guarantees logarithmic height log(n) which in turn ensures logarithmic
        insertion and removal.

    Max Heap (Heap Invariant):
        - All parent nodes are larger than both the child nodes, with the root being the largest.
        - Left child does not need to be less than right child like in a BST.
        - Gives us O(_01_BasicPython) access to max/min

    Min Heap:
        - All parent nodes are smaller than the child nodes with the root being the smallest


We have a few Heap Operations that are important:

    - Heapify built into the constructor and called if we use arr=[...], else we initialise an empty queue.
    - Insert and swim up, O(logn), eg add at end and heapify.
    - Delete and sink down, O(n) since we must search array for the value, swap, delete and then heapify.
    - Extract Min O(_01_BasicPython) but heapify after is O(logn)
    - Contains O(n), search the array.


"""
from datetime import datetime


class PriorityQueue(object):

    def __init__(self, arr=None):
        if arr is None:
            self.arr = []
        else:
            self.arr = arr
            for i in range(len(self.arr)-1, -1, -1):
                self.swim(i)                            # initialise empty heap or heapify existing array
        self.n = len(self.arr)                          # size of the heap
        self.log = []                                   # log of all actions occurring

    # method for adding value to the Min Heap
    def insert(self, value):
        self.log.append((value, "Inserted", datetime.now()))
        self.arr.append(value)
        self.n += 1
        index = self.n - 1
        self.swim(index)

    # method to remove a value from the Min Heap
    def delete(self, value):
        exists = self.contains(value)
        if exists is False:
            print("{} doesn't exist".format(value))
            return
        self.log.append((value, "Removed", datetime.now()))
        index = self.find_value(value)
        last_index = self.n - 1
        self.swap(index, last_index)
        self.n -= 1
        self.arr.pop()
        self.sink(index)

    # method to show the Heap
    def show(self):
        print(self.arr)

    # method to peek at next in queue
    def peek(self):
        print(self.arr[0])

    # method to check if the Min Heap is a Min Heap
    def is_min_heap(self):
        flag = True
        for i in range(len(self.arr)):
            if self.next_priority(i) != i:
                flag = False
                return flag
        return flag

    # method to extract the next value in the queue
    def extract_min(self):
        if self.is_empty() is True:
            print("Queue is empty")
            return
        next = self.arr[0]
        self.log.append((next, "Queue Pop", datetime.now()))
        self.delete(next)
        return next

    # helper function to check if value exists in the heap
    def contains(self, value):
        flag = False
        for i in range(len(self.arr)):
            if self.arr[i] == value:
                flag = True
                return flag
        return flag

    # helper function to check if heap is empty
    def is_empty(self):
        if len(self.arr) == 0:
            return True
        else:
            return False

    # helper function to find index of a value
    def find_value(self, value):
        for i in range(self.n):
            if self.arr[i] == value:
                return i

    # helper function to swap values
    def swap(self, ind1, ind2):
        self.arr[ind1], self.arr[ind2] = self.arr[ind2], self.arr[ind1]

    # helper function to swim a value up the heap if needed
    def swim(self, index):
        current_index = index
        parent_index = (index - 1)//2
        if parent_index >= 0 and self.arr[current_index] < self.arr[parent_index]:
            self.swap(current_index, parent_index)
            self.swim(parent_index)
        else:
            return

    # helper function to sink a value down the heap if needed
    def sink(self, index):
        current_index = index
        swap_index = self.next_priority(current_index)
        if current_index != swap_index:
            self.swap(current_index, swap_index)
            self.sink(swap_index)
        else:
            return

    # helper function to find the index of the next in line of a parent and its children
    def next_priority(self, index):
        priority = index
        left_child_index = (index*2) + 1
        right_child_index = (index*2) + 2
        if left_child_index < self.n and self.arr[left_child_index] < self.arr[priority]:
            priority = left_child_index
        if right_child_index < self.n and self.arr[right_child_index] < self.arr[priority]:
            priority = right_child_index
        return priority

q = PriorityQueue(arr=[4, 1, 3, 2, 16, 9, 10, 14, 8, 7])
q.show()
print(q.is_min_heap())



# q = PriorityQueue()
# q.insert(10)
# q.show()
# q.insert(6)
# q.show()
# q.insert(11)
# q.show()
# q.insert(7)
# q.show()
# q.insert(2)
# q.show()
# q.insert(3)
# q.show()
# print(q.is_min_heap())
# print(q.contains(2))
# print(q.contains(9))
# q.delete(9)
# q.peek()
# q.delete(2)
# q.show()
# q.peek()
# print(q.extract_min())
# q.show()
# print(q.extract_min())
# q.show()
# print(q.extract_min())
# q.show()
# print(q.extract_min())
# q.show()
# print(q.extract_min())
# q.show()
# print(q.extract_min())
# q.show()