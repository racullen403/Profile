"""
We are given 2 non-empty linked lists where each node is a
positive digit and the list represents the reverse order of the integer

    e.g     4 -> 6 -> 9 would represent 964

We are tasked with adding two of these lists and returning the integer as another
linked list.

Solution 1:
    - We can solve this a very straight forward way by iterating through each list and calculating the total, and then
    simply using % and // to create the new linked list of the total

Solution 2:
    - We can apply the same method but condense it a bit into one pass through the lists.
    - We total the current digits of the lists, insert total%10 into the new linked list, and then carry the total//10
    over to the next set of digits in the lists, do this until we have gone through all digits and the total is 0:

    e.g  1 -> 2 -> 3
         4 -> 8 -> 5

         add 1 and 4 to the total, total = 5 so output for this digit is 5 and total become 0 again

         add 2 and 8 to total, total = 10, so output for this digit is 0 however total become 1 now

         add 3 and 5 to total, total = 9, so output for this digit is 9 and total become 0

         since l1 and l2 and done, and the total=0, we are finished, output -> 0-> 1 -> 9 or 910
"""


class Node:

    def __init__(self, digit=None):
        self.data = digit
        self.next = None

    def show(self):
        temp = self
        while temp:
            print(temp.data, "-->", end=" ")
            temp = temp.next
        print("END")


# Solution 1
def add_two_nums(l1, l2):
    total = 0
    i = 0
    while l1:
        total += l1.data * (10**i)
        l1 = l1.next
        i += 1
    i = 0
    while l2:
        total += l2.data * (10**i)
        l2 = l2.next
        i += 1
    output = Node()
    temp = output
    while total != 0:
        temp.next = Node(digit=(total % 10))
        temp = temp.next
        total = total // 10
    return output.next


# Solution 2
def alt_add_two_nums(l1, l2):
    total = 0
    output = ListNode()
    temp = output
    while l1 or l2 or total:
        if l1:
            total += l1.val
            l1 = l1.next
        if l2:
            total += l2.val
            l2 = l2.next
        temp.next = ListNode(val=total % 10)
        total //= 10
        temp = temp.next
    return output.next


def example_add_two_nums():
    print("---------------Expected-----------------")
    print("Lists: l1=6->7->8 and l2=9->3->4 \nTotal=876+439=1315  \nReturn List:5->1->3->1")
    print("---------------Solution-----------------")
    l1 = Node(6)
    l1.next = Node(7)
    l1.next.next = Node(8)
    l2 = Node(9)
    l2.next = Node(3)
    l2.next.next = Node(4)
    print("l1: ", end="")
    l1.show()
    print("l2: ", end="")
    l2.show()
    print("l1 + l2:", end=" ")
    add_two_nums(l1, l2).show()

