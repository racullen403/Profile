"""
We are tasked to swap all adjacent pairs of nodes in a linked list

                (1) - (2) - (3) - (4)
    becomes:
                (2) - (1) - (4) - (3)
"""


class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def swap_adjacent_nodes(head):
    output = ListNode()
    temp = output
    temp.next = head
    while temp.next and temp.next.next:
        s1 = temp.next
        s2 = temp.next.next
        s1.next = s2.next
        s2.next = s1
        temp.next = s2
        temp = s1
    return output.next


