"""
_328_OddEvenLinkedList

Given a linked list, we want to return the list with the odd index nodes first, and the even index nodes second,

    e.g. 1 - 2 - 3- 4 - 5 - 6  becomes 1 - 3 - 5 - 2 - 4 - 6

This must be done in O(1) space complexity (ie we cannot just form two list and attach them, it must be done in place),
and in O(n) time complexity.


    Solution:
        - We simply need to keep track of the end of the even list and the end of the odd lists

            (O) - (E) - (O) - (E) - ...
            o      e     i     i.next

            o is odd list end, e is even list end and i is the next node to look at

        In the general case:
        - attach i.next to e.next and move e to e.next
        - attach i to o.next and move o to o.next
        - attach the head of the even list to the end of odd
        - set i as the next term after the even list

        We are done when i is None

"""


class Node:

    def __init__(self, val):
        self.val = val
        self.next = None


# create linked list
def create_list():
    head = Node("O")
    temp = head
    for i in range(4):
        temp.next = Node("E")
        temp.next.next = Node("O")
        temp = temp.next.next
    return head


# show initial list
def show_list(lst):
    temp = list
    while lst:
        print("({})".format(lst.val), end=" -> ")
        lst = lst.next
    print()


# sort evens and odds
def odd_even_list(lst):
    if not lst:
        return
    o = lst
    e = lst.next
    while e and e.next:
        i = e.next
        e.next = i.next
        e = e.next
        i.next = o.next
        o.next = i
        o = o.next


def example1():
    print("Linked List:")
    lst = create_list()
    show_list(lst)
    print("Sort List Even and Odd:")
    odd_even_list(lst)
    show_list(lst)


def example2():
    lst = Node(1)
    temp = lst
    for i in range(2, 10):
        temp.next = Node(i)
        temp = temp.next
    print("Linked List:")
    show_list(lst)
    print("Sorted Odd and Even:")
    odd_even_list(lst)
    show_list(lst)


