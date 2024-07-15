class ListNode():

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next 

def removeNthNode(head, n):
    """
    Medium: Remove the Nth node from the end of the list, ie 0 would return head, 1 would remove the last node, 2 removes the 2nd last etc

    Sol:    - Have a front runner node that runs n places ahead of the slower node.
            - If front reaches the end and is it None, check that i == n, if so we remove the first node, else, n is too large and we remove nothing. 
            - Move slow and front 1 step at a time until front reaches the last node.
            - Slow is now one position before the node that needs removes (so remove it)
    """
    if n == 0:
        return head
    
    front = head
    i = 0
    while i < n and front:
        front = front.next
        i += 1

    if not front:
        if n == i:
            return head.next 
        return head
    
    slow = head
    while front.next:
        slow = slow.next
        front = front.next

    slow.next = slow.next.next

    return head


