"""
This is a Binary Heap that lets us index the data structure (for priority queues).

We use Mapping for O(1) look up times, instead of searching a full array which is O(n):
    - We map the key to its positional index using a dictionary and then positional index back to the key
    (pm is positional map, im is inverse map).

        eg  pm = {key:[position_index, priority], ...}
            im = {positional_index: key, ...}

    - Now consider contains() method, before we would have to search the entire heap O(n) to see if a value is
    in the heap, now to see if the value say 5 exists, we just have to check if 5 exists in the pm dictionary,
    this is O(_01_BasicPython) time.

Methods for MinHeap Priority Queue:
    - Insert, O(logn)
    - Delete, from end O(_01_BasicPython), specific key O(logn)
    - Extract Min, getting the Min is O(_01_BasicPython) but the heapify after is O(logn)
    - Contains O(_01_BasicPython)
    - Change Priority O(logn)
"""
from datetime import datetime


# We will use dictionary to store keys, priorities, positional map, and inverse mapping
# Currently you must create the Queue from the ground up, I will implement a heapify method for an array
class IndexPriorityQueue(object):

    def __init__(self):
        self.pm = {}            # mapping key to its position index and priority level, {key: [i, prio], ...}
        self.im = {}            # mapping index in heap to its key, {i: key}
        self.n = 0              # tracker for the size of heap
        self.log = []           # log to keep track of all actions occurring, (key, datetime, action)

    # method to insert key at end of heap, and swim it up if necessary
    def q_insert(self, key, priority):
        self.log.append((key, "Inserted with priority {}.".format(priority), datetime.now()))
        insert_index = self.n
        self.pm[key] = [insert_index, priority]
        self.im[insert_index] = key
        self.n += 1
        self.swim(key)

    # method to delete a key from the heap
    def q_delete(self, key, reason="Manually removed."):
        self.log.append((key, reason, datetime.now()))
        delete_index = self.pm[key][0]
        last_index = self.n - 1
        if delete_index == last_index:
            self.pm.pop(key)
            self.im.pop(last_index)
            self.n -= 1
            return
        self.swap(delete_index, last_index)
        swapped_key = self.im[delete_index]
        self.pm.pop(key)
        self.im.pop(last_index)
        self.n -= 1
        self.sink(swapped_key)

    # method to remove next key from queue and remove it
    def q_extract_min(self):
        if self.is_empty() is True:
            return
        min_key = self.im[0]
        self.q_delete(min_key, "Extract Min")
        return min_key

    # method to change the priority of a key and update the heap
    def change_priority(self, key, priority):
        current_index = self.pm[key][1]
        self.pm[key][1] = priority
        self.log.append((key, "Update priority from {} to {}.".format(current_index, priority), datetime.now()))
        if priority < current_index:
            self.swim(key)
        elif priority > current_index:
            self.sink(key)
        else:
            return

    # method to show next in queue
    def q_peek(self):
        print("Key: " + str(self.im[0]) + "   Priority: " + str(self.pm[self.im[0]][1]))

    # method to see all keys in the queue and their priority
    def q_show(self):
        for i in range(self.n):
            print("Key: " + str(self.im[i]) + "   Priority: " + str(self.pm[self.im[i]][1]))

    # method to check if our heap is a Min Heap
    def is_min_heap(self):
        flag = True
        for i in range(self.n):
            next_priority_index = self.min_child(self.im[i])
            if next_priority_index != i:
                flag = False
                break
        return flag

    # method to check if a key exists
    def q_contains(self, key):
        if key in self.pm:
            return True
        else:
            return False

    # recursive helper function to compare a key with its parent and swim it up if needed, continues until
    # in correct place or at root position
    def swim(self, key):
        current_index = self.pm[key][0]
        parent_index = (current_index - 1) // 2
        if current_index > 0 and self.pm[self.im[current_index]][1] < self.pm[self.im[parent_index]][1]:
            self.swap(current_index, parent_index)
            self.swim(key)
        else:
            return

    # recursive  helper function to compare key with its children and sink it down if needed, continues until
    # in correct place or at a leaf position
    def sink(self, key):
        next_priority_index = self.min_child(key)
        current_index = self.pm[key][0]
        if next_priority_index != current_index:
            self.swap(current_index, next_priority_index)
            self.sink(key)
        else:
            return

    # helper function to return the index of the highest priority of some key and its children
    def min_child(self, key):
        current_index = self.pm[key][0]
        left_child_index = (current_index*2) + 1
        right_child_index = (current_index*2) + 2
        highest_priority_index = current_index
        if left_child_index < self.n and self.pm[self.im[left_child_index]][1] < self.pm[self.im[highest_priority_index]][1]:
            highest_priority_index = left_child_index
        if right_child_index < self.n and self.pm[self.im[right_child_index]][1] < self.pm[self.im[highest_priority_index]][1]:
            highest_priority_index = right_child_index
        return highest_priority_index

    # helper function to swap the position indices in our mapping of a parent and child
    def swap(self, ind1, ind2):
        self.pm[self.im[ind1]][0], self.pm[self.im[ind2]][0] = self.pm[self.im[ind2]][0], self.pm[self.im[ind1]][0]
        self.im[ind1], self.im[ind2] = self.im[ind2], self.im[ind1]

    # helper function to stop process if queue is empty
    def is_empty(self):
        if self.n == 0:
            return True
        else:
            return False


