"""
Medium: Given 2D array, points for the (x, y) plane, and integer k, return the k closest points to the origin (0, 0).

Sol:
    - Create a min heap with the distances for each point, map these points to the coordinates to return.
"""
import heapq
import math

def kClosest(points, k):
    heap = [] 
    lookup = {}
    for x, y in points:
        dist = math.sqrt(x**2 + y**2)
        if dist not in lookup:
            lookup[dist] = [] 
        lookup[dist].append((x,y))
        heap.append(dist)
    heapq.heapify(heap)    # O(n) sort for min heap using sift down method.
    res = [] 
    while heap and k > 0:
        dist = heapq.heappop(heap)
        res.append(lookup[dist].pop())
        k -= 1
    return res

    