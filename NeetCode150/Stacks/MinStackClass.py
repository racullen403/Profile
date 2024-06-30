# Medium: the only hard part is keeping track of the minimum in O(1) time. This is achieved during the push,
# we check if the new value being pushed at that index is less than the previous min, and append the 
# corresponding new min or old min. ie stack [3, 1, 2, 4, 0], min [3, 1, 1, 1, 0].

class MinStack:

    def __init__(self):
        self.stack = []
        self.min = []
    
    def push(self, val):
        self.stack.append(val)
        if self.min:
            val = min (val, self.min[-1])
        self.min.append(val)

    def pop(self):
        if self.stack:
            self.stack.pop()
            self.min.pop()

    def top(self):
        if self.stack:
            return self.stack[-1]
        
    def getMin(self):
        if self.stack:
            return self.min[-1]
        