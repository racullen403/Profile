"""
The Stack is a linear structure that follows a Last In First Out approach. Simply think of it as stacking plates,
you can only access the most recent plate that has been stacked.


Stack data structure:

    - We need to define a size for the stack (not in python, but for other languages), and a pointer to tell us how
    many objects are in the stack.

    - We need to be able to push objects into the stack, and remove/pop them out

    Our implementation of the stack below is how it would actually work, be would have a predefined array and simply
    update the values in those memory locations, while moving a pointer to tell us where the top of the stack
    currently is. In python this is more trivial since we don't have to define out variable types, output types, and
    array sizes.

The Stack space complexity is just the size chosen at creation, it will always remain this size since we use a pointer
to say where the "top" of the stack is, the objects in the stack beyond "top" still exist, they are just ignored.

The time complexity of all push/pop are O(1) as we are just moving a pointer.
"""


class MyStack:

    def __init__(self, size=10):
        self.stack = [0]*size
        self.top = -1
        self.size = size

    def push(self, val):
        if not self.is_full():
            self.top += 1
            self.stack[self.top] = val
        else:
            raise ValueError("Stack is full!")

    def pop(self):
        if not self.is_empty():
            output = self.stack[self.top]
            self.top -= 1
            return output
        else:
            raise ValueError("Stack is empty!")

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.size - 1

    def show(self):
        print("\nTop:", self.top)
        print("[", end="")
        for i in range(self.size):
            if i < self.size - 1:
                print("({}){},".format(i, self.stack[i]), end=" ")
            else:
                print("({}){}".format(i, self.stack[i]), end="")
        print("]")


