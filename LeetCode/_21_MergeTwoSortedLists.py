"""
Given 2 sorted linked lists, we are tasked with merging them.

Solution:
    - Simply create another list with a temp node that moves along and attach the
    smaller node of the two. When one of the lists reaches the end, we attach the other
    list
"""


class Node:
    def __init__(self):
        self.val = None
        self.next = None


def merge_sorted_lists(l1, l2):
    # Create output list and a cursor to move along it (temp)
    output = Node()
    temp = output
    while l1 and l2:
        if l1.val <= l2:
            temp.next = l1
            l1 = l1.next
        else:
            temp.next = l2
            l2 = l2.next
        temp = temp.next
    if l1:
        temp.next = l1
    else:
        temp.next = l2
    return output.next
