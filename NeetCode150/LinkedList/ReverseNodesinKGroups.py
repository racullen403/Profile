"""
Hard: Given a linked list and an positive integer k, reverse the nodes in groups of size k, ie 12345678 -> 32165478

Sol:
    - Create new output list and temp pointer to track it.
    - Move to the kth position to check if we have a valid group.
    - Use pointer at start of group to add nodes with temp to the output, stop when we reach end of group.
    - Repeat until we cant reverse any groups.
"""

class ListNode():
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next 


def reverseKGroup(head, k):
    output = ListNode()
    temp = output
    rev = head      # Nodes to be put in reverse order
    while rev:
        front = rev     # Check valid group of k
        for _ in range(k-1):
            front = front.next 
            if not front:       # not valid so we dont reverse remaining nodes, attach them and return
                temp.next = rev
                return output.next
        new_group = front.next  # simply attach nodes into the reverse ordering, moving rev forward until it reaches the new grouping
        while rev != new_group:
            store = temp.next 
            temp.next = rev 
            rev = rev.next 
            temp.next.next = store
        while temp.next:       # move temp to the end of the output list, ready to attach next group
            temp = temp.next
    return output.next


        
             