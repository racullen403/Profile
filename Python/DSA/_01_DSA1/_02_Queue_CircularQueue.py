"""
A Queue functions how you would imagine a real life queue works, the first person into it should be the first
person out, this is called First In First Out.

This implementation would simply require a front and rear pointer, this way we know if the queue is full or not, and
know how to enqueue and dequeue.

Since we are predefining the size of the queue, we can only enqueue while the rear pointer is < size of the array, this
means even if there is space at the front of the array after a dequeue, we can't use it.

To get around this, we introduce the "Circular Queue". This uses the front and rear pointers like a queue, however, if
there is empty space in front of the "front" pointer, we can enqueue into.

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



