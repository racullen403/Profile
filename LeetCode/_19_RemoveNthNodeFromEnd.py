"""
Given a linked list we want to remove the nth node from the end.

Solution:
    - We need to find a way of getting the node before the nth from the end. The slow
    way would be to count through all the nodes, then count again to the nth from the
    end.
    - The faster method is to use a runner node at the front that counts n nodes ahead of a
    trailing node, when the runner reaches the last node, the trailing node should be at the
    desired place.


    Ex:
        Remove 2nd from end:

        1 -> 2 -> 3 -> 4 -> 5       Linked List

        (F) Front node
        (T) Trail node

        count = 0
        HEAD -> 1   ->   2  ->   3  ->   4  ->  5   ->  NONE
        (F)  ->

        count = 1
        HEAD -> 1   ->   2  ->   3  ->   4  ->  5   ->  NONE
               (F)

        count = 2, insert Trailing node and continue until (F) at end
        HEAD -> 1   ->   2  ->   3  ->   4  ->  5   ->  NONE
        (T)             (F)


        HEAD -> 1   ->   2  ->   3  ->   4  ->  5   ->  NONE
               (T)              (F)

        HEAD -> 1   ->   2  ->   3  ->   4  ->  5   ->  NONE
                        (T)              (F)

        HEAD -> 1   ->   2  ->   3  ->   4  ->  5   ->  NONE
                                (T)            (F)

        We see (F) -> NONE, so it has reached the end and (T) points to the 2nd from last
        node as required
"""


class Node:

    def __init__(self):
        self.value = None
        self.next = None


def remove_nth_from_last_node(linkedlist, n):
    # Case 1
    # n=0, we don't remove anything
    if n == 0:
        return linkedlist
    front = linkedlist
    for i in range(n):
        front = front.next
    # Case 2
    # Front node is beyond the last node, e.g. front=None, this means n was the length of
    # the list, we are removing the first node
    if front is None:
        return linkedlist.next
    # Case 3, we are removing some middle node
    trail = linkedlist
    while front.next:
        front = front.next
        trail = trail.next
    trail.next = trail.next.next
    return linkedlist