class ListNode():

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next 

"""
Medium: Reorder for general case [0, 1, 2, 3, ..., n-2, n-1] ---> [0, n-1, 1, n-2, 2, n-3, ...]
"""
def reorderList(head):
    print("\nHead:", end=" ")
    show(head)
    # We get slow to point to the middle
    slow = head
    fast = head.next 
    while fast and fast.next :
        slow = slow.next 
        fast = fast.next.next

    # We reverse the last terms
    reverse = ListNode() 
    temp = slow.next
    slow.next = None 
    while temp:
        store = reverse.next 
        reverse.next = temp
        temp = temp.next 
        reverse.next.next = store
    reverse = reverse.next
    print("Reverse:", end=" ")
    show(reverse)
    
    # Now we have head [0, 1, 2, 3, 4, 5, 6] and reverse [6, 5, 4], simply iterate until reverse is in place
    res = ListNode()
    temp = res 
    while reverse:
        temp.next = head 
        head = head.next 
        temp = temp.next 
        temp.next = reverse
        reverse = reverse.next
        temp = temp.next 
    
    # There will either be 1 heade item left, or none
    if head:
        temp.next = head 

    return res.next


def create(arr):
    res = ListNode()
    temp = res
    for a in arr:
        temp.next = ListNode(a)
        temp = temp.next
    return res.next

def show(node):
    temp = node
    while temp:
        print(temp.val, "-->", end=" ")
        temp = temp.next
    print("None")


def test():
    arr = [2, 4, 6, 8, 10]
    node = create(arr)
    show(node)
    show(reorderList(node))
