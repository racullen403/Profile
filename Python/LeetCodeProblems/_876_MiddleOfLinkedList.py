"""
876 Middle of Linked List

Given a linked list, we want to return the middle node, if even number of nodes then return 2nd middle node


    Solution:
        - We iterate through the linked list with a front/runner pointer, and use a trailing pointer to find the middle.
        - The trailing pointer simply needs to moved forward one node for every 2 the runner goes through, this way
        when the runner reaches the end, the trailing pointer will stop in the middle.


"""


class Node:

    def __init__(self, val):
        self.val = val
        self.next = None


def create_list(n):
    lst = Node(1)
    if n <= 1:
        return lst
    temp = lst
    for i in range(2, n):
        temp.next = Node(i)
        temp = temp.next
    return lst


def find_middle_list(lst):
    if not lst:
        return
    runner = lst
    trailer = lst
    move = True
    while runner.next:
        if move:
            trailer = trailer.next
            move = False
        else:
            move = True
        runner = runner.next
    return trailer


# show initial list
def show_list(lst):
    temp = list
    while lst:
        print("({})".format(lst.val), end=" -> ")
        lst = lst.next
    print()


def example():
    lst = create_list(11)
    show_list(lst)
    print("Middle Node ({})".format(find_middle_list(lst).val))


example()
