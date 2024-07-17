import heapq
""" 
Easy: Create class to find kth largest integer in a stream of values (includes duplicates)

Sol:
    - Implement a min heap of size k, that way the first term is always the kth largest after we pop out all terms before it
"""

# My own implementation of a min heap included, otherwise import heapq
class KthLargest():

    def __init__(self, k, nums):
        self.k = k
        self.minHeap = nums
        self.minheapify()
        while len(nums) > k:
            self.pop()

    def add(self, val):
        self.push(val)
        if len(self.minHeap) > self.k:
            self.pop()
        print(self.minHeap[0])
        return self.minHeap[0]
    
    def pop(self):
        if len(self.minHeap):
            self.minHeap[0], self.minHeap[-1] = self.minHeap[-1], self.minHeap[0]
            self.minHeap.pop()
            self._minheapify(0)

    def push(self, val):
        self.minHeap.append(val)
        i = len(self.minHeap) - 1
        parent = (i - 1) // 2
        while i > 0 and self.minHeap[parent] > self.minHeap[i]:
            self.minHeap[i], self.minHeap[parent] = self.minHeap[parent], self.minHeap[i]
            i = parent
            parent = (i - 1) // 2

    def _minheapify(self, i):
        start = (len(self.minHeap) - 1) // 2
        if i > start:
            return
        l = (i * 2) + 1
        r = (i * 2) + 2
        index = i
        if l < len(self.minHeap) and self.minHeap[index] > self.minHeap[l]:
            index = l
        if r < len(self.minHeap) and self.minHeap[index] > self.minHeap[r]:
            index = r 
        if index == i:
            return
        self.minHeap[i], self.minHeap[index] = self.minHeap[index], self.minHeap[i]
        self._minheapify(index)
    
    def minheapify(self):
        start = (len(self.minHeap) - 1) // 2
        for i in range(start, -1, -1):
            self._minheapify(i)

    def show(self):
        print("heap", self.minHeap)


class KthLargestEasy():

    def __init__(self, k , nums):
        self.k = k 
        self.heap = nums
        heapq.heapify(self.heap)    # import heapq
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val):
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]


def test():
    nums = [i for i in range(16, 0, -1)]
    print("nums", nums)
    heap = KthLargest(6, nums)
    heap.show()
    print(heap.add(16))
    heap.show()
    print(heap.add(16))
    heap.show()
    print(heap.add(16))
    heap.show()
    print(heap.add(16))
    heap.show()

