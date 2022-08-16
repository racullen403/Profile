from ProgamizDSA.Subjects.Trees.AVLTree import AVL
from random import shuffle


def create_tree():
    t1 = AVL()
    mylist = list(range(10))
    shuffle(mylist)
    for i in mylist:
        print("\n-------------")
        t1.insert(i)
        print("Insert:", i, "\n")
        t1.show()
    print("Is tree balanced:", t1.is_balanced())
    return t1


my_tree = create_tree()
my_tree.delete(my_tree.head.val)
my_tree.show_tree_detail(my_tree.head, "", True)
print(my_tree.is_balanced())