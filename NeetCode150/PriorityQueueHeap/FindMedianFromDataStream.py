"""
Hard: Create a way to add numbers from a stream of integers, and find the median so far.

Sol:
    - We use a minHeap to add larger numbers to, and a maxHeap to add the smaller numbers two.
    - If we maintain the sizes of the 2 heaps, then the top of the heaps will allow use to find the median.
"""
import heapq

class FindMedian():

    def __init__(self):
        self.minHeap = []   # Contains the larger numbers
        self.maxHeap = []   # Contains the -ve smaller numbers

    def addNumber(self, num):
        if self.minHeap and num > self.minHeap[0]:  # Case when num is larger than the smallest of the larger numbers
            heapq.heappush(self.minHeap, num)
        else:                                       # Only Other Case
            heapq.heappush(self.maxHeap, -1 * num)
        if len(self.minHeap) > len(self.maxHeap) + 1:   # Size of larger nums is more than 1 item larger than smaller, pop and swap
            heapq.heappush(self.maxHeap, -1 * heapq.heappop(self.minHeap))
        elif len(self.maxHeap) > len(self.minHeap) + 1: # Other case
            heapq.heappush(self.minHeap, -1 * heapq.heappop(self.maxHeap))

    def findMedian(self):
        if len(self.maxHeap) > len(self.minHeap):
            return -1 * self.maxHeap[0]
        elif len(self.minHeap) > len(self.maxHeap):
            return self.minHeap[0]
        else:
            return (self.minHeap[0] + (-1 * self.maxHeap[0])) / 2.0