"""
Monotone Stack:

    The standard Monotone Stack is a way of obtaining the monotonically increasing/decreasing values from an array in
    O(n) time

        e.g [1, 5, 3, 4, 2, 6, 8, 7]  -> [1, 3, 4, 6, 7]

"""


class MonotoneStack:

    def __init__(self, array):
        self.arr = array
        self.increasing_array = self.monotonically_increase()
        self.decreasing_array = self.monotonically_decrease()

    def monotonically_increase(self):
        arr = self.arr
        stack = []
        for i in range(len(arr)):
            while len(stack) and stack[-1] > arr[i]:
                stack.pop()
            stack.append(arr[i])
        return stack

    def monotonically_decrease(self):
        arr = self.arr
        stack = []
        for i in range(len(arr)):
            while len(stack) and stack[-1] < arr[i]:
                stack.pop()
            stack.append(arr[i])
        return stack

    def show(self):
        print("Input Array:", self.arr)
        print("Increasing:", self.increasing_array)
        print("Decreasing:", self.decreasing_array)


def example():
    a = [9, 1, 4, 2, 8, 3, 7, 6, 5]
    monotone_a = MonotoneStack(a)
    monotone_a.show()

