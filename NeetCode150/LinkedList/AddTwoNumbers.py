class ListNode:

    def __init__(self, val=0, next=None):
        self.val = val 
        self.next = next 


def addTwoNumbers(l1, l2):
    """"
    Medium: Given 2 non-empty lists representing non-negative integers, stored in reverse order (3-2-1 represent 123), 
    with no leading 0's, return their sum as a list representation

    Sol:
        - Track remainder term throughout, at each digit position simply add digits and remainder, then input the digit and carry over remainder.
        - Move along lists like this until we reach end, then proceed as before for any list remaining
        - Check for one last remainder term to be added on the end of list.
    
    """
    rem = 0
    output = ListNode()
    temp = output
    while l1 and l2:
        node = ListNode()
        total = rem + l1.val + l2.val
        digit = total % 10
        rem = total // 10
        node.val = digit
        temp.next = node 
        temp = temp.next
        l1 = l1.next 
        l2 = l2.next 
    while l1:
        node = ListNode()
        total = rem + l1.val 
        digit = total % 10
        rem = total // 10
        node.val = digit
        temp.next = node 
        temp = temp.next
        l1 = l1.next 
    while l2: 
        node = ListNode()
        total = rem + l2.val
        digit = total % 10
        rem = total // 10
        node.val = digit
        temp.next = node 
        temp = temp.next
        l2 = l2.next 
    if rem:
        temp.next = ListNode(rem)
    return output.next


def cleanerTwoNumbers(l1, l2):
    rem = 0 
    output = ListNode()
    temp = output 
    while l1 or l2 or rem:
        v1 = l1.val if l1 else 0 
        v2 = l2.val if l2 else 0 

        total = rem + v1 + v2
        digit = total % 10 
        rem = total // 10 

        temp.next = ListNode(digit)

        temp = temp.next 
        l1 = l1.next if l1 else None 
        l2 = l2.next if l2 else None 

    return output.next