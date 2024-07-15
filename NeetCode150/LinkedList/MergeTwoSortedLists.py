class ListNode():

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next 

def mergeTwoSortedLists(list1, list2):
    l1 = list1 
    l2 = list2 
    res = ListNode()
    temp = res
    while l1 and l2:
        if l1.val < l2.val:
            temp.next = l1 
            l1 = l1.next
        else:
            temp.next = l2 
            l2 = l2.next 
        temp = temp.next 
    if l1:
        temp.next = l1 
    if l2:
        temp.next = l2
    return res.next