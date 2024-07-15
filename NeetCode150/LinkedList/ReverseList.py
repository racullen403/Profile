class ListNode():

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next 

def reverseList(head):
    res = ListNode()
    temp = head
    while temp:
        store = res.next            # Store whats attached to result
        res.next = temp             # Update new first term of result with next item in LL
        temp = temp.next            # Move pointer to next item in LL 
        res.next.next = store       # Attach previous reversed list to new first item in list
    return res.next
        

        
