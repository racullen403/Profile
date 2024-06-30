"""
Given K sorted Linked Lists, we want to merge them into one Linked List (all ascending order)


Solution 1, Sorting:

    - We go through each of the lists, adding the nodes into a new list.
    - We then sort the new list based on the node.val
    - Simply connect the nodes from start to finish

Solution 2:

    - Just the same but we use a min heap for sorting

"""
import heapq


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Solution 1
def merge_k_lists(lists):
    nodes = []
    for l in lists:
        while l:
            nodes.append(l)
            l = l.next
    nodes.sort(key=lambda x: x.val)
    output = ListNode()
    temp = output
    for node in nodes:
        temp.next = node
        temp = temp.next
    return output.next


# Solution 2
def merge_k_list_with_heap(lists):
    nodes = []
    index = 0
    for l in lists:
        while l:
            heapq.heappush(nodes, (l.val, index, l))
            l = l.next
            index += 1
    output = ListNode()
    temp = output
    while nodes:
        temp.next = heapq.heappop(nodes)[2]
        temp = temp.next
    return output.next

