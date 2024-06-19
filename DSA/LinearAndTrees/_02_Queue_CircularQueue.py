"""
Queue:

    A Queue functions how you would imagine a real life queue works, the first person into it should be the first
    person out, this is called First In First Out.

    This implementation would simply require a front and rear pointer, this way we know if the queue is full or not,
    and know how to enqueue and dequeue.

    Since we are predefining the size of the queue, we can only enqueue while the rear pointer is < size of the array,
    this means even if there is space at the front of the array after a dequeue, we can't use it.

Circular Queue:

    To get around this, we introduce the "Circular Queue". This uses the front and rear pointers like a queue, however,
    if there is empty space in front of the "front" pointer, we can enqueue into.

    The space complexity is defined at the time of creating the queue and remains constant.

    The time complexity of enqueue and dequeue are O(1)


Uses of Queues:

    CPU and Disk Scheduling

    Handling interrupts in real time systems

    General queue usage, to queue phone calls, game login's, requests for data etc...


Class Example:

    E.G.    Define: cq = MyCircularQueue(size=3)  cq -> Front = -1, Rear = -1, queue = [0, 0, 0]

            Dequeue when empty:  cq.dequeue() would raise value error "Queue is Empty"

            Enqueue:  cq.enqueue(True)  cq -> Front = 0, Rear = 0, queue = [True, 0, 0]
                      cq.enqueue(False) cq -> Front = 0, Rear = 1, queue = [True, False, 0]
                      cq.enqueue(6)     cq -> Front = 0, Rear = 2, queue = [True, False, 6]

            Enqueue when full: cq.enqueue(_) would raise ValueError "Queue is Full"

            Dequeue:  cq.dequeue()     cq -> Front = 1, Rear = 2, queue = [True, False, 6]  returns True
                      cq.dequeue()     cq -> Front = 2, Rear = 2, queue = [True, False, 6]  returns False

            Enqueue   cq.enqueue(43)   cq -> Front = 2, Rear = 0, queue = [43, False, 6]

            If front and rear are equal, the next dequeue will reset the pointers to -1 to signify the queue is empty.

"""


class MyCircularQueue:

    def __init__(self, size=10):
        self.queue = [0]*size
        self.front = -1
        self.rear = -1
        self.size = size

    def is_empty(self):
        return self.front == -1

    def is_full(self):
        if (self.front == 0 and self.rear == self.size - 1) or (self.front - self.rear == 1):
            return True
        return False

    def enqueue(self, val):
        if self.is_empty():
            self.front = 0
            self.rear = 0
            self.queue[0] = val
        elif self.is_full():
            raise ValueError("Queue is full!")
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = val

    def dequeue(self):
        if self.is_empty():
            raise ValueError("Queue is empty!")
        else:
            output = self.queue[self.front]
            if self.front == self.rear:
                self.front = -1
                self.rear = -1
            else:
                self.front = (self.front + 1) % self.size
            return output

    def show(self):
        print("\nFront:", self.front, "Rear:", self.rear)
        print("[", end="")
        for i in range(self.size):
            if i < self.size - 1:
                print("({}){},".format(i, self.queue[i]), end=" ")
            else:
                print("({}){}".format(i, self.queue[i]), end="")
        print("]\n")



def example_full():
    q = MyCircularQueue(size=5)
    for obj in [4, 5, 2, 6, 7, 8]:
        q.enqueue(obj)
        q.show()

def example_circle():
    q = MyCircularQueue(size=5)
    for obj in [4, 5, 2, 6, 7]:
        q.enqueue(obj)
        q.show()
    print("Is q full:", q.is_full())
    print("\nDequeue 2 objs")
    for _ in range(2):
        q.dequeue()
        q.show()
    print("\nEnqueue 2 objs and see how rear now moves towards from of list")
    for obj in ["obj1", "REAR"]:
        q.enqueue(obj)
        q.show()

example_circle()