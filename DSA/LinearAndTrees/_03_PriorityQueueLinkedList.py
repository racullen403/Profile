"""
A priority queue assigns a priority value to each element in the queue, elements with the highest priority will
dequeue first, and elements with the same priority will dequeue in the order they entered the queue.

Implementation:

    - We can create a priority queue using a linked list, in our case, a lower number indicates a higher priority

        e.g.    priority queue looks something like:

                [ (1)A ] -> [ (1)B ] -> [ (1)C ] -> [ (2)D ]  -> [ (2)E ]

                where A is the object in the queue, (1) is its priority, and [ ... ] represents the Node pointing
                to the next Node in queue.

                if we enqueue, say F with priority (1) it would be placed as follows

                [ (1)A ] -> [ (1)B ] -> [ (1)C ] -> [ (1)F ] -> [ (2)D ]  -> [ (2)E ]


                If we want to dequeue, we simply take the front Node from the list.

    - Insertion into Linked List is O(n), dequeue is O(1)

"""


class PriorityQueueListNode:

    def __init__(self, val, priority=0):
        self.val = val
        self.priority = priority
        self.next = None


class PriorityQueueList:

    def __init__(self, node=None):
        self.head = node

    def is_empty(self):
        return self.head is None

    def enqueue(self, val, priority):
        node = PriorityQueueListNode(val, priority)
        if self.is_empty():
            self.head = node
        else:
            temp = self.head
            if priority < temp.priority:
                node.next = temp
                self.head = node
            else:
                while temp.next and temp.next.priority <= priority:
                    temp = temp.next
                node.next = temp.next
                temp.next = node

    def dequeue(self):
        if self.is_empty():
            raise ValueError("Queue is empty!")
        else:
            temp = self.head
            self.head = temp.next
            return temp.val

    def show(self):
        print("\nPriority Queue:")
        if self.is_empty():
            print("EMPTY!")
        else:
            temp = self.head
            while temp:
                print("[ ({}){} ] ->".format(temp.priority, temp.val), end=" ")
                temp = temp.next
            print("END!")


def example():
    pq = PriorityQueueList()
    objects = [(1, "A"), (1, "B"), (1, "C"), (2, "D"), (3, "E"), (1, "F"), (0, "G")]
    for obj in objects:
        pq.enqueue(obj[1], obj[0])
        pq.show()

example()