"""
Medium: Given array of CPU tasks, tasks where tasks[i] is a letter "A"-"Z", and an integer n, return the minimum CPU cycles to complete all tasks.

    - A CPU cycle will complete one task, and they can be completed in any order.
    - Identical tasks must be separated by n cycles

Sol:
    - If task "A" needs run 3 times, and task "B" needs run 2 times, logically we want to run A - B - idle/run other tasks until A - B again.
    - Count all the tasks and map them to their counts.
    - Then going through the counts we schedule all tasks with most duplicates, and store their duplicates in a queue for n cycles before adding back to 
    the heap.
    - This can be done by storing the counts in a maxHeap, and storing the duplicates in a queue.
            - Take from queue first if the item has been there for n cycles and add back to heap.
            - If item in queue is not ready, we take from heap, this involves either idle for a cycle if not item in heap, or taking the item, scheduling it, 
            reduce count by 1 and add to the queue for n cycles.
            - Continue like this until heap and queue are empty.
"""
import heapq

def leastInterval(tasks, n):
    counts = {}
    for t in tasks:
        if not t in counts:
            counts[t] = 0
        counts[t] += 1
    print("Counts", counts)
    heap = []
    for k in counts:
        heap.append(-counts[k])
    heapq.heapify(heap) # maxHeap of counts for each unique task (using -ve counts)
    print("Heap", heap)
    q = []  # Queue
    qi = 0  # index for position we are at in the queue
    time = 0
    while heap or qi < len(q):
        time += 1
        print("  time", time)
        if qi < len(q) and q[qi][0] == time:    # Item in queue and has been there for n cycles, add back to heap
            print("    take item from q and add to heap")
            heapq.heappush(heap, q[qi][1])
            qi += 1
        if not heap:  # Not items in heap and items in q are not ready for schedule
            print("    idle")
            continue
        else:   # We schedule item from heap, if it has duplicates (count is not -1) then add to queue for n cycles with new count
            cnt = heapq.heappop(heap)
            cnt += 1
            print("    take item from heap")
            if cnt != 0:
                q.append([time + n + 1, cnt])
                print("    add item to q")
    return time


def test():
    tasks = ["A", "A", "A", "B", "B", "C"]
    t = ["X","X","Y","Y"]
    leastInterval(t, 2)

test()

            