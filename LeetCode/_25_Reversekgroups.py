"""
We are given a linked list and asked to reverse groups of k nodes,

 i.e    k = 2,  list = 1 -> 2 -> 3 -> 4 -> 5

                reversed list = 2 -> 1 -> 4 -> 3 -> 5


        k = 3,  list = 1 -> 2 -> 3 -> 4 -> 5

                reversed list = 3 -> 2 -> 1 -> 4 -> 5


Solution 1:

    - We keep count of nodes, using r, and stop when we have counted k. We keep track of the starting node using l.

        e.g     k = 3

                        1 -> 2 -> 3 -> 4 -> 5
                        l              r            count = 3

    - We then need to reverse these first k, use new pointers, curr = l for the current node being placed correctly,
    and new = r for the reversed list we are creating

        - 1) Store curr.next,    store = (2) - (3) -

        - 2) Attach new to curr,  curr = (1) - (4) - (5) and makes this, new = (1) - (4) - (5)

        - 3) make curr the stored node, curr = (2) - (3) -

        - 4) We repeat this k=3 times, ending up with:

                new = (3) - (2) - (1) - (4) - (5)

            using some pointer "temp" for the output, we attach "new", temp.next = new, and move this pointer to the
            new correct position, temp = l = (1)-..., now move starting pointer l = r and repeat


Solution 2, using stack:

    - Simply iterate through nodes adding them to a list, if the list reaches length k, then pop and attach them
    to the output, when we have iterated through all nodes, simply attach the first node remaining in the list.


Solution 3, Recursion:

    - Check to make sure there are k nodes left, else return remaining nodes.
    - We apply our same swapping process, but only do it for one group.
    - We set the last node of the group, node.next = recursion(remaining nodes)
    - return the node we want attached to node.next

"""


class ListNode(object):
     def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Solution 1
def reverse_k_nodes(head, k):
    output = ListNode()
    temp = output
    r = head
    l = head
    while True:
        count = 0
        while r and count < k:
            count += 1
            r = r.next
        if count < k:
            return output.next
        else:
            curr = l
            new = r
            for _ in range(k):
                store = curr.next
                curr.next = new
                new = curr
                curr = store
            temp.next = new
            temp = l
            l = r


# Solution 2
def reverse_k_nodes_stack(head, k):
    if k == 1:
        return head
    output = ListNode()
    temp = output
    nodes = []
    while head:
        nodes.append(head)
        head = head.next
        if len(nodes) == k:
            while nodes:
                temp.next = nodes.pop()
                temp = temp.next
    if nodes:
        temp.next = node[0]
    else:
        temp.next = None
    return output.next


# Solution 3
def reverse_k_nodes_recursive(head, k):
    # Check for k nodes, else return the < k nodes
    temp = head
    for _ in range(k):
        if not temp:
            return head
        temp = temp.next
    # curr is current node we are placing into correct position
    # new is the reversed list being made
    curr = head
    new = None
    for _ in range(k):
        store = curr.next
        curr.next = new
        new = curr
        curr = store
    # head is now the last node in the reverse list,
    # we attach the solution of the remaining nodes starting from curr
    head.next = reverse_k_nodes_recursive(curr, k)
    return new
