"""
A Linked List is a linear structure that is a series of Nodes that point to the next Node:

    E.G.    Root: [ Node1 ] -> [Node2 ] -> ... -> [ NodeN ] -> NONE

            Root is the pointer to the first Node (it's address) in the linked list, NONE signifies the end
            of the list.


There are different types of linked lists:
    - Singly, Nodes only point to the next.
    - Doubly, Nodes point to the next and to the previous
    - Circular, can be singly or doubly linked list but the final Node will point back to the root completing the circle.


Below we have created a Singly Linked List but the basic idea is the same for all types:
    - The advantage of a linked list over the array is we can break the links at some point and rejoin it again,
    this allows us to remove nodes without having to shift the remaining ones like in an array.
    - We can remove nodes in O(n) time by searching through the list for the value to remove.
    - Our implementation of insert below requires us to traverse through the list to the end before inserting,
    taking O(n) time. This can easily be changed to O(1) by having a pointer to the final Node in the list. Check
    comments of LinkedList class to see.

"""


class ListNode:

    def __init__(self, val=None):
        self.val = val
        self.next = None


class LinkedList:

    def __init__(self, ):
        self.root = None
        # self.end = self.root

    def insert(self, val):

        if not self.root:
            self.root = ListNode(val)
            # self.end = self.root
        else:
            # self.end.next = ListNode(val)
            # self.end = self.end.next DONE
            # Below is the traversal
            temp = self.root
            while temp.next:
                temp = temp.next
            temp.next = ListNode(val)

    def remove(self, val):
        if not self.root:
            raise ValueError("List is empty")
        else:
            temp = ListNode()
            temp.next = self.root
            while temp.next and temp.next != val:
                temp = temp.next
            if not temp.next:
                raise ValueError("Could not find {}".format(val))
            else:
                # if temp.next == self.end:
                #     self.end = temp
                temp.next = temp.next.next