"""
A Deque is a Double-Ended Queue, we can insert and remove from both ends of the queue.

We can implement it similar to how we made the Circular Queue, with a rear and front pointer.

Note in python we don't need to define the size of the deque, but for better understanding we will.

"""


class Deque:

    def __init__(self, size=10):
        self.deque = [0]*size
        self.front = -1
        self.rear = -1
        
    def is_empty(self):
        return self.front == -1

    def is_full(self):
        if self.front - self.rear == 1 or (self.front == 0 and self.rear == len(self.deque)-1):
            return True
        return False

    def insert_front(self, val):
        if self.is_full():
            raise ValueError("Deque is full!")
        elif self.is_empty():
            self.front = 0
            self.rear = 0
            self.deque[0] = val
        else:
            self.front -= 1
            if self.front == -1:
                self.front = len(self.deque) - 1
            self.deque[self.front] = val

    def insert_rear(self, val):
        if self.is_full():
            raise ValueError("Deque is full!")
        elif self.is_empty():
            self.front = 0
            self.rear = 0
            self.deque[0] = val
        else:
            self.rear = (self.rear + 1) % len(self.deque)
            self.deque[self.rear] = val

    def remove_front(self):
        if self.is_empty():
            raise ValueError("Deque is empty")
        else:
            temp = self.deque[self.front]
            self.front = (self.front + 1) % len(self.deque)
            return temp

    def remove_rear(self):
        if self.is_empty():
            raise ValueError("Deque is empty")
        else:
            temp = self.deque[self.rear]
            self.rear -= 1
            if self.rear == -1:
                self.rear = len(self.deque) - 1
            return temp
