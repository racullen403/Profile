""" 
Easy: Given an array of integers, stones, representing the weights of stones. Run the following simulation:
    - At each step choose the 2 heaviest stones, x and y, smash them together.
    - If x == y they are destroyed.
    - If x < y then stone x is destroyed and the stone y now has weight y-x.
    Continue until there are no more than 1 stone remaining, return the weight of the last stone.

Sol:
    - Sounds like a basic Max Heap where we pop the first 2 then add the possible result back, with some additional logic.

"""
import heapq

def lastStoneWeight(stones):
    heap = [-s for s in stones] # convert to -ve as heapq is minheap
    heapq.heapify(heap) # O(n) sort
    while len(heap) > 1:
        x = heapq.heappop(heap)
        y = heapq.heappop(heap)
        if x < y:
            heapq.heappush(heap, x - y)
    if len(heap) == 0:
        return 0
    return abs(heap[0])


def test():
    stones = [2,3,6,2,4]
    lastStoneWeight(stones)


test()
        