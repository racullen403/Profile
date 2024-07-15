def hasCycle(head):
    """
    Easy: Given a linked list, return true/false if their is a cycle in the list

    Sol:
        - Add nodes visited into a set/map, if we find it again, we are in a cycle

        - To reduce memory, we can use a slow and fast pointer method
        - slow moves 1 node, fast moves 2 nodes at a time.
        - If there is no cycle, fast reaches None and we are done.
        - If there is a cycle, the distance between fast and slow will decrease by 1 on every step, this is because fast becomes 
        2 places closer to slow and slow moves 1 place away from fast in a cycle, and so will always catch up in linear time.
    """
    lookup = {} 
    temp = head 
    while temp:
        if temp in lookup:
            return True 
        lookup[temp] = True 
        temp = temp.next 
    return False

def hasCycle2(head):
    fast, slow = head, head 
    while fast and fast.next: 
        fast = fast.next.next 
        slow = slow.next 
        if fast == slow:
                return True 
    return False