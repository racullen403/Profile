from BinarySearchTree import Node, BST


t1 = BST()
t1.show()
a = [5,3,1,4,9,10,7,8]
for i in a:
    print("\nInsert", i)
    t1.insert(i)
    t1.show()


b = [5,3,1,4,9,10,7,8]
t2 = BST()
t2.build_bst(b)
t2.show()

t1.is_tree_bst()
t2.is_tree_bst()


t3 = BST()
t3.head = Node(10)
t3.head.left = Node(9)
t3.head.right = Node(8)
t3.is_tree_bst()

print("\n---------------")
t1.show()
print(t1.search(9))

t1.delete_node(5)
print("\n---------------")
t1.show()


print("\n---------------")
print("Head height:", t1.get_node_height(t1.head))
print("Node(1) height:", t1.get_node_height(t1.head.left.left))
print("Is Head balanced:", t1.is_node_balanced(t1.head))
print("Is t1 balanced:", t1.is_tree_balanced())