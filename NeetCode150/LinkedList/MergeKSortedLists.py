"""
Hard: Given k sorted lists, we want to merge them into 1 sorted linked list.

Sol:
    - We already know how to do a mergesort of two linked lists.
    - We couple the lists and merge 2 at a time, halving the k lists, repeat this until we are left with on list
    - Results in us sorting the n nodes log(k) times so O(n.logk) time complexity
    
"""



class ListNode():

    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next 


def mergeKLists(lists):

    if not lists or len(lists) == 0:
        return None
    
    def merge(l1, l2):
        output = ListNode()
        temp = output 
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
        else:
            temp.next = l2
        return output.next
    
    while len(lists) > 1:
        new_lists = []
        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i+1] if i+1 < len(lists) else None 
            new_lists.append(merge(l1, l2))
        lists = new_lists

    return lists[0]


